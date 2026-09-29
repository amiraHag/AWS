import numpy as np


def sigmoid(x):
    """Calculate sigmoid"""
    return 1 / (1 + np.exp(-np.array(x, dtype=float)))


# ─────────────────────────────────────────────
#  SIGMOID NOTEBOOK GRADERS
# ─────────────────────────────────────────────

def grade_h(h, x, w):
    """Grade: linear combination of inputs and weights (h = x · w)"""
    answer = np.dot(x, w)
    if h == answer:
        print("✅ Good job! `h` is correct.")
    else:
        print("❌ Try again. `h` is not correct.")


def grade_nn_output(nn_output, x, w):
    """Grade: sigmoid output of neural network"""
    answer = sigmoid(np.dot(x, w))
    if nn_output == answer:
        print("✅ Good job! `nn_output` is correct.")
    else:
        print("❌ Try again. `nn_output` is not correct.")


def grade_error(error, y, nn_output, x, w):
    """Grade: error = y - nn_output"""
    nn_output_answer = sigmoid(np.dot(x, w))
    answer = y - nn_output_answer
    if error == answer:
        print("✅ Good job! `error` is correct.")
    else:
        print("❌ Try again. `error` is not correct.")


def grade_error_term(error_term, y, x, w):
    """Grade: error_term = error * nn_output * (1 - nn_output)"""
    nn_output_answer = sigmoid(np.dot(x, w))
    error_answer = y - nn_output_answer
    answer = error_answer * nn_output_answer * (1 - nn_output_answer)
    if error_term == answer:
        print("✅ Good job! `error_term` is correct.")
    else:
        print("❌ Try again. `error_term` is not correct.")


def grade_del_w(del_w, learnrate, y, x, w):
    """Grade: weight update = learnrate * error_term * x"""
    nn_output_answer = sigmoid(np.dot(x, w))
    error_answer = y - nn_output_answer
    answer = learnrate * error_answer * nn_output_answer * (1 - nn_output_answer) * x
    if np.array_equal(del_w, answer):
        print("✅ Good job! `del_w` is correct.")
    else:
        print("❌ Try again. `del_w` is not correct.")


# ─────────────────────────────────────────────
#  BACKPROPAGATION NOTEBOOK GRADERS
# ─────────────────────────────────────────────

def grade_output_error(error, target, output):
    """Grade: output error = target - output"""
    answer = target - output
    if error == answer:
        print("✅ Well done! `error` is correct.")
    else:
        print("❌ Try again. `error` is not correct.")


def grade_output_error_term(output_error_term, error, output):
    """Grade: output error term = error * output * (1 - output)"""
    answer = error * output * (1 - output)
    if output_error_term == answer:
        print("✅ Well done! `output_error_term` is correct.")
    else:
        print("❌ Try again. `output_error_term` is not correct.")


def grade_hidden_error_term(hidden_error_term, output_error_term, weights_hidden_output, hidden_layer_output):
    """Grade: hidden error term = (output_error_term · W_ho) * h * (1 - h)"""
    answer = (np.dot(output_error_term, weights_hidden_output)
              * hidden_layer_output * (1 - hidden_layer_output))
    if np.array_equal(hidden_error_term, answer):
        print("✅ Well done! `hidden_error_term` is correct.")
    else:
        print("❌ Try again. `hidden_error_term` is not correct.")


def grade_delta_w_h_o(delta_w_h_o, learnrate, output_error_term, hidden_layer_output):
    """Grade: Δw (hidden→output) = learnrate * output_error_term * hidden_layer_output"""
    answer = learnrate * output_error_term * hidden_layer_output
    if np.array_equal(delta_w_h_o, answer):
        print("✅ Well done! `delta_w_h_o` is correct.")
    else:
        print("❌ Try again. `delta_w_h_o` is not correct.")


def grade_delta_w_i_h(delta_w_i_h, learnrate, hidden_error_term, x):
    """Grade: Δw (input→hidden) = learnrate * hidden_error_term * x (outer product)"""
    answer = learnrate * hidden_error_term * x[:, None]
    if np.array_equal(delta_w_i_h, answer):
        print("✅ Well done! `delta_w_i_h` is correct.")
    else:
        print("❌ Try again. `delta_w_i_h` is not correct.")


# ─────────────────────────────────────────────
#  IMPLEMENT BACKPROPAGATION NOTEBOOK GRADER
# ─────────────────────────────────────────────

def grade_implement_backprop(weights_input_hidden, weights_hidden_output,
                              features_test, targets_test, threshold=0.70):
    """
    Grade the full backpropagation implementation by evaluating
    test-set accuracy of the trained weights.

    Parameters
    ----------
    weights_input_hidden  : trained input→hidden weight matrix
    weights_hidden_output : trained hidden→output weight vector
    features_test         : test feature DataFrame / array
    targets_test          : test target Series / array
    threshold             : minimum accuracy to pass (default 0.70)
    """
    hidden = sigmoid(np.dot(features_test, weights_input_hidden))
    out = sigmoid(np.dot(hidden, weights_hidden_output))
    predictions = out > 0.5
    accuracy = np.mean(predictions == targets_test)
    print(f"Prediction accuracy: {accuracy:.3f}")
    if accuracy > threshold:
        print("✅ Nice job! Your backpropagation implementation is correct.")
    else:
        print(f"❌ Accuracy too low ({accuracy:.3f} < {threshold}). "
              "Check your forward pass, error terms, and weight update steps.")


# ─────────────────────────────────────────────
#  IMPLEMENT GRADIENT DESCENT NOTEBOOK GRADER
# ─────────────────────────────────────────────

def grade_implement_gd(weights, features_test, targets_test, threshold=0.70):
    """
    Grade the full gradient descent implementation by evaluating
    test-set accuracy of the trained weights.

    Parameters
    ----------
    weights       : trained weight vector
    features_test : test feature DataFrame / array
    targets_test  : test target Series / array
    threshold     : minimum accuracy to pass (default 0.70)
    """
    out = sigmoid(np.dot(features_test, weights))
    predictions = out > 0.5
    accuracy = np.mean(predictions == targets_test)
    print(f"Prediction accuracy: {accuracy:.3f}")
    if accuracy > threshold:
        print("✅ Nice job! Your gradient descent implementation is correct.")
    else:
        print(f"❌ Accuracy too low ({accuracy:.3f} < {threshold}). "
              "Check your output, error, error_term, and weight update steps.")


# ─────────────────────────────────────────────
#  PERCEPTRONS NOTEBOOK GRADERS
# ─────────────────────────────────────────────

def grade_hidden_layer(hidden_layer_in, hidden_layer_out, X,
                        weights_input_to_hidden):
    """
    Grade: forward pass through the hidden layer.
      hidden_layer_in  = X · weights_input_to_hidden
      hidden_layer_out = sigmoid(hidden_layer_in)
    """
    ans_in  = np.dot(X, weights_input_to_hidden)
    ans_out = sigmoid(ans_in)

    ok_in  = np.array_equal(hidden_layer_in,  ans_in)
    ok_out = np.array_equal(hidden_layer_out, ans_out)

    if ok_out:
        print("✅ Good job! `hidden_layer_out` is correct.")
    else:
        if not ok_in:
            print("❌ Try again. `hidden_layer_in` is not correct — "
                  f"expected {ans_in}.")
        print("❌ Try again. `hidden_layer_out` is not correct — "
              f"expected {ans_out}.")


def grade_output_layer(output_layer_in, output_layer_out,
                        hidden_layer_out, weights_hidden_to_output):
    """
    Grade: forward pass through the output layer.
      output_layer_in  = hidden_layer_out · weights_hidden_to_output
      output_layer_out = sigmoid(output_layer_in)
    """
    ans_in  = np.dot(hidden_layer_out, weights_hidden_to_output)
    ans_out = sigmoid(ans_in)

    ok_in  = np.array_equal(output_layer_in,  ans_in)
    ok_out = np.array_equal(output_layer_out, ans_out)

    if ok_out:
        print("✅ Good job! `output_layer_out` is correct.")
    else:
        if not ok_in:
            print("❌ Try again. `output_layer_in` is not correct — "
                  f"expected {ans_in}.")
        print("❌ Try again. `output_layer_out` is not correct — "
              f"expected {ans_out}.")
