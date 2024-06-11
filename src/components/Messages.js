export default function Messages({numAsk}) {
    let res = [];
    for(let i = 1; i <= numAsk; i++) {
        res.push(
            <>
                { (localStorage[`answer${i - 1}`] && localStorage[`answer${i - 1}`][1])
                    ? <div className='chat-block' key={'ans' + i}>
                        <div className='message'>
                            {JSON.parse( localStorage.getItem(`answer${i-1}`) )[1]}
                        </div>
                    </div>
                    : ''
                }

                {(i < 4)
                    ? <div className='chat-block ask' key={'ask' + i}>
                        <div className='message'>
                            {JSON.parse( localStorage.getItem(`answer${i}`) )[0]}
                        </div>
                    </div>
                    : ''
                }
            </>
        )
    }
    return res
}