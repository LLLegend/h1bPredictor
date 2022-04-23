export default {
    // 默认请求成功
    DEFAULT_SUCCESS: {
        code: 200,
        message: ''
    },
    // 默认请求失败
    DEFAULT_ERROR: {
        code: 188,
        message: '系统错误'
    },
    // 定义错误返回-缺少必要参数
    LACK: {
        code: 199,
        message: '缺少必要参数'
    },
    // 定义错误返回-Token验证失败
    TOKEN_ERROR: {
        code: 401,
        message: 'Token验证失败'
    },
    // 定义错误返回-用户名或密码错误
    LOGIN_ERROR: {
        code: 101,
        message: '用户名或密码错误'
    },
}
