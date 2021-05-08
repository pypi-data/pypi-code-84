import os
import nnvis
import logging
import copy
import torch
import numpy as np
import scipy.interpolate
from pathlib import Path
from numpy.polynomial import Polynomial


logger = logging.getLogger("vis_net")


def convert_list2str(int_list):
    """
    Helper function. Converts list of ints to char string.

    :param int_list: list to be converted
    :return: converted string
    """
    res = int(''.join(map(str, int_list)))

    return res


class Examinator1D:
    def __init__(self, model, device, alpha, final_state_path, init_state_path):
        self.model = model
        self.device = device
        self.alpha = alpha
        self.theta = copy.deepcopy(torch.load(final_state_path))
        self.theta_f = copy.deepcopy(torch.load(final_state_path))
        self.theta_i = copy.deepcopy(torch.load(init_state_path))

        logger.debug(f"Model: "
                     f"{model}")
        logger.debug(f"Device: {device}")
        logger.debug(f"Alpha: {alpha}")
        logger.debug(f"Final state path: {final_state_path}")
        logger.debug(f"Init state path: {init_state_path}")

    def calc_distance(self, layer, idxs=None):
        """
        Method calculates distance between initial and final parameters

        :param layer: layer
        :param idxs: position of parameter
        :return: distance
        """
        if not idxs:
            return torch.dist(self.theta_f[layer], self.theta_i[layer])
        else:
            return torch.dist(self.theta_f[layer][idxs], self.theta_i[layer][idxs])


class Linear(Examinator1D):
    def __calc_theta_single(self, layer, idxs, alpha):
        """
        Method calculates interpolation of a single parameter with respect to interpolation coefficient alpha

        :param layer: layer of parameter
        :param idxs: position of parameter
        :param alpha: interpolation coefficient
        """
        logger.debug(f"Calculating: {layer} {idxs} for alpha = {alpha}")

        self.theta[layer][idxs] = (self.theta_i[layer][idxs] * (1.0 - alpha)) + (
                    self.theta_f[layer][idxs] * alpha)

        logger.debug(f"Modified theta:\n"
                     f"{self.theta[layer][idxs]}")

    def __calc_theta_vec(self, layer, alpha):
        """
        Method calculates the value of parameters on the level of layer at an interpolation point alpha,
        using the linear interpolation.

        :param layer: layer
        :param alpha: interpolation coefficient
        """
        logger.debug(f"Calculating: {layer} for alpha = {alpha}")

        self.theta[layer] = torch.add((torch.mul(self.theta_i[layer], (1.0 - alpha))),
                                      torch.mul(self.theta_f[layer], alpha))

    def interpolate_all_linear(self, test_loader):
        """
        Method interpolates all parameters of the model and after each interpolation step evaluates the
        performance of the model

        :param test_loader: test loader loader
        """

        if not nnvis.loss_path.exists() or not nnvis.acc_path.exists():
            v_loss_list = []
            acc_list = []
            layers = [name for name, _ in self.model.named_parameters()]

            self.model.load_state_dict(self.theta_f)
            for alpha_act in self.alpha:
                for layer in layers:
                    self.__calc_theta_vec(layer, alpha_act)
                    self.model.load_state_dict(self.theta)

                loss, acc = nnvis.test(self.model, test_loader, self.device)
                v_loss_list.append(loss)
                acc_list.append(acc)

            np.savetxt(nnvis.loss_path, v_loss_list)
            np.savetxt(nnvis.acc_path, acc_list)
            self.model.load_state_dict(self.theta_f)

    def individual_param_linear(self, test_loader, layer, idxs):
        """
        Method interpolates individual parameter of the model and evaluates the model after each interpolation
        step

        :param test_loader: test loader
        :param layer: layer
        :param idxs: position of the parameter
        """

        loss_res = Path("{}_{}_{}".format(nnvis.svloss_path, layer, convert_list2str(idxs)))
        loss_img = Path("{}_{}_{}".format(nnvis.svloss_img_path, layer, convert_list2str(idxs)))

        acc_res = Path("{}_{}_{}".format(nnvis.sacc_path, layer, convert_list2str(idxs)))
        acc_img = Path("{}_{}_{}".format(nnvis.sacc_img_path, layer, convert_list2str(idxs)))

        dist = Path("{}_{}_{}_{}".format(nnvis.svloss_path, layer, convert_list2str(idxs), "distance"))

        logger.debug(f"Result files:\n"
                     f"{loss_res}\n"
                     f"{acc_res}\n")
        logger.debug(f"Img files:\n"
                     f"{loss_img}\n"
                     f"{acc_img}\n")
        logger.debug(f"Dist file:\n"
                     f"{dist}\n")

        if not loss_res.exists() or not acc_res.exists():
            logger.debug("Files with results not found - beginning interpolation.")

            v_loss_list = []
            acc_list = []

            self.model.load_state_dict(self.theta_f)
            for alpha_act in self.alpha:
                self.__calc_theta_single(layer + ".weight", idxs, alpha_act)

                self.model.load_state_dict(self.theta)

                logger.debug(f"Getting validation loss and accuracy for alpha = {alpha_act}")
                val_loss, acc = nnvis.test(self.model, test_loader, self.device)
                acc_list.append(acc)
                v_loss_list.append(val_loss)

            logger.debug(f"Saving results to files ({loss_res}, {acc_res})")

            np.savetxt(loss_res, v_loss_list)
            np.savetxt(acc_res, acc_list)
            self.model.load_state_dict(self.theta_f)

        if not dist.exists():
            logger.info(f"Calculating distance for: {layer} {idxs}")

            distance = self.calc_distance(layer + ".weight", idxs)
            logger.info(f"Distance: {distance}")

            with open(dist, 'w') as fd:
                fd.write("{}".format(distance))

        logger.debug(f"Saving results to figures {loss_img}, {acc_img} ...")

        nnvis.plot_metric(self.alpha, np.loadtxt(loss_res), loss_img, "loss")
        nnvis.plot_metric(self.alpha, np.loadtxt(acc_res), acc_img, "acc")

        self.model.load_state_dict(self.theta_f)

        return

    def layers_linear(self, test_loader, layer):
        """
        Method interpolates parameters of selected layer of the model and evaluates the model after each interpolation
        step

        :param test_loader: test loader
        :param layer: layer to be interpolated
        """

        loss_res = Path("{}_{}".format(nnvis.vvloss_path, layer))
        loss_img = Path("{}_{}".format(nnvis.vvloss_img_path, layer))

        acc_res = Path("{}_{}".format(nnvis.vacc_path, layer))
        acc_img = Path("{}_{}".format(nnvis.vacc_img_path, layer))

        dist = Path("{}_{}_{}".format(nnvis.vvloss_path, layer, "distance"))

        logger.debug(f"Result files:\n"
                     f"{loss_res}\n"
                     f"{acc_res}")
        logger.debug(f"Img files:\n"
                     f"{loss_img}\n"
                     f"{acc_img}")
        logger.debug(f"Dist file:\n"
                     f"{dist}")

        if not loss_res.exists() or not acc_res.exists():
            logger.debug("Result files not found - beginning interpolation.")

            v_loss_list = []
            acc_list = []

            self.model.load_state_dict(self.theta_f)
            for alpha_act in self.alpha:
                self.__calc_theta_vec(layer + ".weight", alpha_act)
                self.__calc_theta_vec(layer + ".bias", alpha_act)

                self.model.load_state_dict(self.theta)
                logger.debug(f"Getting validation loss and accuracy for alpha = {alpha_act}")

                vloss, acc = nnvis.test(self.model, test_loader, self.device)
                v_loss_list.append(vloss)
                acc_list.append(acc)

            logger.debug(f"Saving results to files ({loss_res}, {acc_res})")
            np.savetxt(loss_res, v_loss_list)
            np.savetxt(acc_res, acc_list)

        if not dist.exists():
            logger.info(f"Calculating distance for: {layer}")

            distance = self.calc_distance(layer + ".weight")
            logger.info(f"Distance: {distance}")

            with open(dist, 'w') as fd:
                fd.write("{}".format(distance))

        logger.debug(f"Saving results to figures {loss_img}, {acc_img} ...")
        nnvis.plot_metric(self.alpha, np.loadtxt(loss_res), loss_img, "loss")
        nnvis.plot_metric(self.alpha, np.loadtxt(acc_res), acc_img, "acc")

        self.model.load_state_dict(self.theta_f)

        return


class Quadratic(Examinator1D):
    def __calc_theta_single_q(self, layer, idxs, alpha, start, mid, end):
        """
        Method calculates quadratic interpolation of a single parameter with respect to interpolation coefficient
        alpha

        :param layer: layer of parameter
        :param idxs: position of parameter
        :param alpha: interpolation coefficient value
        :param start: first point
        :param mid: second point
        :param end: ending point
        """
        logger.debug(f"Calculating quadr: {layer} {idxs} for alpha = {alpha}")
        xdata = np.array([start[0], mid[0], end[0]])
        logger.debug(f"XDATA: {xdata}")
        ydata = np.array([start[1], mid[1], end[1]])
        logger.debug(f"YDATA: {ydata}")

        poly = scipy.interpolate.lagrange(xdata, ydata)

        self.fit_params = Polynomial(poly).coef
        logger.debug(f"Coefficients: {self.fit_params}")

        try:
            self.theta[layer][idxs] = torch.tensor((self.fit_params[0]*(alpha**2) + self.fit_params[1]*alpha +
                                                   self.fit_params[2])).to(self.device)
        except IndexError:
            return
        logger.debug(f"Modified theta:\n"
                     f"{self.theta[layer][idxs]}")

    def __calc_theta_vec_q(self, layer, alpha, start, mid, end):
        """
        Method calculates value of the parameters on the level of layer at an interpolation point alpha,
        using the quadratic interpolation.

        :param layer: examined layer
        :param alpha: actual interpolation coefficient value
        :param start: first known point
        :param mid: second known point
        :param end: last known point
        """
        logger.debug(f"Calculating quadr: {layer} for alpha = {alpha}")
        xdata = [start[0], mid[0], end[0]]
        logger.debug(f"XDATA: {xdata}")

        ydata = [start[1], mid[1], end[1]]
        logger.debug(f"YDATA: {ydata}")

        self.theta[layer] = \
            start[1] * (((alpha - mid[0]) * (alpha - end[0])) / ((start[0] - mid[0]) * (start[0] - end[0]))) + \
            mid[1] * (((alpha - start[0]) * (alpha - end[0])) / ((mid[0] - start[0]) * (mid[0] - end[0]))) + \
            end[1] * (((alpha - start[0]) * (alpha - mid[0])) / ((end[0] - start[0]) * (end[0] - mid[0])))

        logger.debug(f"Modified theta:\n"
                     f"{self.theta[layer]}")

    def interpolate_all_quadratic(self, test_loader):
        """
        Method interpolates all parameters of the model using the quadratic interpolation
        and after each interpolation step evaluates the performance of the model.

        :param test_loader: test data set loader
        """
        if not nnvis.q_loss_path.exists() or not nnvis.q_acc_path.exists():
            v_loss_list = []
            acc_list = []
            layers = [name for name, _ in self.model.named_parameters()]

            start_a = 0
            mid_a = 0.5
            end_a = 1
            logger.debug(f"Start: {start_a}\n"
                         f"Mid: {mid_a}\n"
                         f"End: {end_a}")

            self.model.load_state_dict(self.theta_f)
            for alpha_act in self.alpha:
                for layer in layers:
                    start_p = self.theta_i[layer].cpu()
                    mid_p = copy.deepcopy(
                        torch.load(os.path.join(nnvis.checkpoints, "checkpoint_1"))[layer]).cpu()  # TODO automatic mid
                    end_p = self.theta_f[layer].cpu()

                    start = [start_a, start_p]
                    mid = [mid_a, mid_p]
                    end = [end_a, end_p]

                    self.__calc_theta_vec_q(layer, alpha_act, start, mid, end)
                    self.model.load_state_dict(self.theta)

                loss, acc = nnvis.test(self.model, test_loader, self.device)
                v_loss_list.append(loss)
                acc_list.append(acc)

            np.savetxt(nnvis.q_loss_path, v_loss_list)
            np.savetxt(nnvis.q_acc_path, acc_list)
            nnvis.plot_lin_quad_real()
            self.model.load_state_dict(self.theta_f)

    def individual_param_quadratic(self, test_loader, layer, idxs):
        """
        Method interpolates individual parameter of the model and evaluates the performance of the model when the
        interpolated parameter replaces its original in the parameters of the model

        :param test_loader: test dataset loader
        :param layer: layer of parameter
        :param idxs: position of parameter
        """

        loss_res = Path("{}_{}_{}_q".format(nnvis.svloss_path, layer, convert_list2str(idxs)))
        loss_img = Path("{}_{}_{}_q".format(nnvis.svloss_img_path, layer, convert_list2str(idxs)))

        acc_res = Path("{}_{}_{}_q".format(nnvis.sacc_path, layer, convert_list2str(idxs)))
        acc_img = Path("{}_{}_{}_q".format(nnvis.sacc_img_path, layer, convert_list2str(idxs)))

        logger.debug(f"Result files:\n"
                     f"{loss_res}\n"
                     f"{acc_res}\n")
        logger.debug(f"Img files:\n"
                     f"{loss_img}\n"
                     f"{acc_img}\n")

        if not loss_res.exists() or not acc_res.exists():
            logger.debug("Files with results not found - beginning interpolation.")

            v_loss_list = []
            acc_list = []

            start_a = 0
            mid_a = 0.5
            end_a = 1
            logger.debug(f"Start: {start_a}\n"
                         f"Mid: {mid_a}\n"
                         f"End: {end_a}")

            start_p = self.theta_i[layer + ".weight"][idxs].cpu()
            mid_p = copy.deepcopy(torch.load(Path(os.path.join(nnvis.checkpoints,
                                                               "checkpoint_7"))))[layer + ".weight"][idxs].cpu()  # TODO AUTO MID
            end_p = self.theta_f[layer + ".weight"][idxs].cpu()

            logger.debug(f"Start loss: {start_p}\n"
                         f"Mid loss: {mid_p}\n"
                         f"End loss: {end_p}")

            start = [start_a, start_p]
            mid = [mid_a, mid_p]
            end = [end_a, end_p]
            logger.debug(f"Start: {start}\n"
                         f"Mid: {mid}\n"
                         f"End: {end}")

            self.model.load_state_dict(self.theta_f)
            for alpha_act in self.alpha:
                self.__calc_theta_single_q(layer + ".weight", idxs, alpha_act, start, mid, end)

                self.model.load_state_dict(self.theta)

                logger.debug(f"Getting validation loss and accuracy for alpha = {alpha_act}")
                val_loss, acc = nnvis.test(self.model, test_loader, self.device)
                acc_list.append(acc)
                v_loss_list.append(val_loss)

            logger.debug(f"Saving results to files ({loss_res}, {acc_res})")

            np.savetxt(loss_res, v_loss_list)
            np.savetxt(acc_res, acc_list)
            self.model.load_state_dict(self.theta_f)

        logger.debug(f"Saving results to figures {loss_img}, {acc_img} ...")
        nnvis.plot_metric(self.alpha, np.loadtxt(loss_res), loss_img, "loss")
        nnvis.plot_metric(self.alpha, np.loadtxt(acc_res), acc_img, "acc")

        self.model.load_state_dict(self.theta_f)

        return

    def layers_quadratic(self, test_loader, layer):
        """
        Method examines the parameters on the level of layers using the quadratic interpolation.

        :param test_loader: test data set loader
        :param layer: layer to be examined
        """
        loss_res = Path("{}_{}_q".format(nnvis.vvloss_path, layer))
        loss_img = Path("{}_{}_q".format(nnvis.vvloss_img_path, layer))

        acc_res = Path("{}_{}_q".format(nnvis.vacc_path, layer))
        acc_img = Path("{}_{}_q".format(nnvis.vacc_img_path, layer))

        logger.debug(f"Result files:\n"
                     f"{loss_res}\n"
                     f"{acc_res}")
        logger.debug(f"Img files:\n"
                     f"{loss_img}\n"
                     f"{acc_img}")

        if not loss_res.exists() or not acc_res.exists():
            logger.debug("Result files not found - beginning interpolation.")

            v_loss_list = []
            acc_list = []

            start_a = 0
            mid_a = 0.5
            end_a = 1
            logger.debug(f"Start: {start_a}\n"
                         f"Mid: {mid_a}\n"
                         f"End: {end_a}")

            start_p = self.theta_i[layer + ".weight"].cpu()
            mid_p = copy.deepcopy(torch.load(os.path.join(nnvis.checkpoints, "checkpoint_6"))[layer + ".weight"]).cpu()  # TODO AUTO MID
            end_p = self.theta_f[layer + ".weight"].cpu()

            start_w = [start_a, start_p]
            mid_w = [mid_a, mid_p]
            end_w = [end_a, end_p]

            start_pb = self.theta_i[layer + ".bias"].cpu()
            mid_pb = copy.deepcopy(torch.load(os.path.join(nnvis.checkpoints, "checkpoint_6"))[layer + ".bias"]).cpu()  # TODO AUTO MID
            end_pb = self.theta_f[layer + ".bias"].cpu()

            start_b = [start_a, start_pb]
            mid_b = [mid_a, mid_pb]
            end_b = [end_a, end_pb]

            for alpha_act in self.alpha:
                self.__calc_theta_vec_q(layer + ".weight", alpha_act, start_w, mid_w, end_w)
                self.__calc_theta_vec_q(layer + ".bias", alpha_act, start_b, mid_b, end_b)

                self.model.load_state_dict(self.theta)
                logger.debug(f"Getting validation loss and accuracy for alpha = {alpha_act}")

                vloss, acc = nnvis.test(self.model, test_loader, self.device)
                v_loss_list.append(vloss)
                acc_list.append(acc)

            logger.debug(f"Saving results to files ({loss_res}, {acc_res})")
            np.savetxt(loss_res, v_loss_list)
            np.savetxt(acc_res, acc_list)

        logger.debug(f"Saving results to figures {loss_img}, {acc_img} ...")
        nnvis.plot_metric(self.alpha, np.loadtxt(loss_res), loss_img, "loss")
        nnvis.plot_metric(self.alpha, np.loadtxt(acc_res), acc_img, "acc")

        self.model.load_state_dict(self.theta_f)

        return
