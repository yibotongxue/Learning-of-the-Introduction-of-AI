# Python 中numpy库中的 argmin 函数
在求最小值和最大值中可以使用argmin函数，但更多的还是用最小堆，这里简单介绍一下argmin函数
## 参数及返回值
下面是官方文档的部分内容
```
def argmin(a, axis=None, out=None, *, keepdims=np._NoValue):
    """
    Returns the indices of the minimum values along an axis.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int, optional
        By default, the index is into the flattened array, otherwise
        along the specified axis.
    out : array, optional
        If provided, the result will be inserted into this array. It should
        be of the appropriate shape and dtype.
    keepdims : bool, optional
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one. With this option,
        the result will broadcast correctly against the array.

        .. versionadded:: 1.22.0

```
参数意义， a 可以是 list 类型，也可以是 array 类型；axis是表示求最小值的维度， keepdims 设置为 True 时，返回的将都是一维的，否则，将按照应该返回的维数返回。

下面是官方文档关于返回值的内容
```
    Returns
    -------
    index_array : ndarray of ints
        Array of indices into the array. It has the same shape as `a.shape`
        with the dimension along `axis` removed. If `keepdims` is set to True,
        then the size of `axis` will be 1 with the resulting array having same
        shape as `a.shape`.
```
返回值可能是最小值的下标， a 为 list 类型是，返回的是所有的数中的而最小值的下表，也就是即使是多维数组，也是平铺成一个一维数组。 a 为 array 类型是，如果不设置 axis ，将等同于 list ，否则将按 axis 以 array的形式返回要求维度的最小值的下标。

当最小值有多个时，将返回第一个的下标。
## 其他相关的函数
官方文档列举出其他的相关的函数。
```
    See Also
    --------
    ndarray.argmin, argmax
    amin : The minimum value along a given axis.
    unravel_index : Convert a flat index into an index tuple.
    take_along_axis : Apply ``np.expand_dims(index_array, axis)``
                      from argmin to an array as if by calling min.
```

参考资料：https://github.com/numpy/numpy/blob/v1.26.0/numpy/core/fromnumeric.py#L1236-L1325
