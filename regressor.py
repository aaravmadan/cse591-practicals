
import numpy as np


class regressor(object):
    """
    This is a sample class for miniproject 1.

    Args:
        data: Is a tuple, ``(x,y)``
              ``x`` is a two or one dimensional ndarray ordered such that axis 0 is independent
              data and data is spread along axis 1. If the array had only one dimension, it implies
              that data is 1D.
              ``y`` is a 1D ndarray it will be of the same length as axis 0 or x.

    """



    """
    Feature Scaling done on the x array (Min-max scaling)
    """
    def feature_scaling(self,x):
        return (x-x.min(axis=0))/(x.max(axis=0)-x.min(axis=0))

    """
    Gradient descent implementation including regularization.
    The loop stops when the total cost almost converges or after 10000 iterations
    """
    def gradient_descent(self,x,y,w,alpha,beta):
        prev_cost = 10
        curr_cost = self.get_cost(x,y,w)
        num_iters = 10000
        iter = 0
        while prev_cost - curr_cost > 0.00000001:

            gradient = ((x.T).dot(x.dot(w)-y) + beta*w.T.dot(w))/y.shape[0]

            w = w - alpha*gradient

            prev_cost = curr_cost
            curr_cost = self.get_cost(x, y, w)
            iter += 1
            if iter > num_iters:
                break

        return w

    """
    Returns the total cost for a given set of weights
    """
    def get_cost(self,x,y,w):
        cost = (((y-(x).dot(w)).T.dot(y-(x).dot(w)))/(2*y.shape[0]))[0][0]
        # print "Cost: ",cost
        return cost

    """
    10 fold cross validation performed with 70% data for training and 30% data for validation
    Sets the global weights parameter to the average of all the weights
    """
    def cross_validate(self,x,y):


        split_dim = int(0.7 * x.shape[0])
        # print "Split: ", split_dim
        fin_w = np.zeros((self.x.shape[1], 1))
        for i in range(0,10):
            w = np.random.rand(self.x.shape[1], 1)

            # print fin_w.shape
            rd = np.arange(len(x))
            np.random.shuffle(rd)
            x = x[rd]
            y = y[rd]
            x_train, x_test = x[:split_dim, :], x[split_dim:, :]
            y_train,y_test = y[:split_dim, :], y[split_dim:, :]

            fin_w = np.add(fin_w,self.gradient_descent(x_train, y_train, w, 0.01,0.05))


        self.w = np.divide(fin_w,10.0)
        return


    def __init__(self, data):
        self.x, self.y = data
        # Here is where your training and all the other magic should happen.
        # Once trained you should have these parameters with ready.
        # print self.y

        # print "w: ",self.x.shape

        self.b = np.random.rand(1)
        self.alpha = 0.01
        self.iterations = 1000
        self.x = self.feature_scaling(self.x)
        one_col = np.ones((self.x.shape[0],1))
        # print "one",one_col.shape
        # print "Before",self.x.shape
        self.x = np.append(one_col,self.x,1)
        self.w = np.random.rand(self.x.shape[1], 1)
        # print self.x
        # self.w = self.gradient_descent(self.x, self.y, self.w,self.b,0.1)
        self.cross_validate(self.x,self.y)
        # print "Ws: ",self.w
        # print "b: ",self.b




    def get_params (self):
        """
        Method that should return the model parameters.

        Returns:
            tuple of numpy.ndarray: (w, b).

        Notes:
            This code will return a random numpy array for demonstration purposes.

        """
        # print "Params: ",self.w

        return (self.w[1:], self.w[0])

    def get_predictions (self, x):
        """
        Method should return the outputs given unseen data

        Args:
            x: array similar to ``x`` in ``data``. Might be of different size.

        Returns:
            numpy.ndarray: ``y`` which is a 1D array of predictions of the same length as axis 0 of
                            ``x``
        Notes:
            Temporarily returns random numpy array for demonstration purposes.
        """
        # Here is where you write a code to evaluate the data and produce predictions.

        x = self.feature_scaling(x)
        one_col = np.ones((x.shape[0], 1))
        # print "one",one_col.shape
        # print "Before",self.x.shape
        x = np.append(one_col, x, 1)
        return x.dot(self.w)

if __name__ == '__main__':
    pass
