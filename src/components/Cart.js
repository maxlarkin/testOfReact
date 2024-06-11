export default function Cart({imgObj, index, func, imgs}) {

    function deleteCart(i, imgs) {
        let res = imgs;
        res.splice(i, 1);
        localStorage.setItem('images', JSON.stringify(res));
        func(res)
    }

    return (
        <div className='cart' key={'cart' + index}>
            <div className="img">
                <div className="delete" onClick={() => deleteCart(index, imgs)}>
                    <img id='deleteImg' src={process.env.PUBLIC_URL + '/img/delete.png'} alt="Delete"/>
                </div>

                    <img alt="" src={imgObj.Image}/>

            </div>
            <div className="info">
                <h5>{imgObj.Name}</h5>
                <h5>{imgObj.Price} ₽</h5>
            </div>
            <div className='description'>
                <p>{imgObj.Description}</p>
            </div>
        </div>
    )
}
