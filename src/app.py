"""y\the firs main modele"""



def model(
    value: float, weight: float, bias: float
) -> int | float:
    """
    Args
    ----
        value (Union[int, float]): _description_
        weight (Union[int, float]): _description_
        bias (Union[int, float]): _description_

    Returns
    -------
        Union[int, float]: _description_
    """
    return value * weight + bias
