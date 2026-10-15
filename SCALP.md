# Range-Scalp Bot

*Updated Thu Oct 15 18:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17984 | 15611 | 2373 (28) | 4 | $-5519.98 | -4.9% |
| **+10¢** | 13585 | 10836 | 2749 (40) | 4 | $-5014.28 | -5.9% |
| **+15¢** | 11393 | 8438 | 2955 (59) | 4 | $-4514.31 | -6.3% |
| **+20¢** | 10126 | 7035 | 3091 (77) | 4 | $-3923.55 | -6.2% |
| **+10¢ (15¢ stop)** | 22142 | 22092 | 50 (29) | 3 | $-8562.89 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 18:55 | +10 stop | XRP | DOWN | 0.64 | open |  |
| 10-15 18:52 | +10 stop | ETH | UP | 0.68 | open |  |
| 10-15 18:51 | +5 | BTC | UP | 0.63 | 0.69 | 0.28 |
| 10-15 18:51 | +10 stop | XRP | DOWN | 0.55 | 0.65 | 0.69 |
| 10-15 18:50 | +15 | BTC | UP | 0.57 | 0.73 | 1.28 |
| 10-15 18:50 | +5 | BTC | UP | 0.57 | 0.62 | 0.15 |
| 10-15 18:50 | +10 stop | ETH | UP | 0.69 | 0.54 | -1.83 |
| 10-15 18:50 | +10 | ETH | UP | 0.69 | open |  |
| 10-15 18:50 | +5 | ETH | UP | 0.69 | open |  |
| 10-15 18:50 | +5 | HYPE | UP | 0.66 | 0.73 | 0.36 |
| 10-15 18:49 | +10 stop | BTC | UP | 0.60 | 0.73 | 0.99 |
| 10-15 18:49 | +10 | BTC | UP | 0.60 | 0.73 | 0.99 |
| 10-15 18:49 | +10 stop | HYPE | UP | 0.57 | 0.68 | 0.76 |
| 10-15 18:49 | +20 | HYPE | UP | 0.57 | 0.78 | 1.79 |
| 10-15 18:49 | +15 | HYPE | UP | 0.57 | 0.73 | 1.28 |
| 10-15 18:49 | +10 | HYPE | UP | 0.57 | 0.68 | 0.76 |
| 10-15 18:49 | +5 | HYPE | UP | 0.57 | 0.62 | 0.15 |
| 10-15 18:49 | +10 stop | DOGE | UP | 0.61 | open |  |
| 10-15 18:49 | +5 | BTC | UP | 0.61 | 0.67 | 0.27 |
| 10-15 18:49 | +5 | ETH | UP | 0.64 | 0.70 | 0.28 |
| 10-15 18:48 | +5 | SOL | UP | 0.65 | 0.72 | 0.39 |
| 10-15 18:48 | +10 stop | ETH | UP | 0.55 | 0.70 | 1.17 |
| 10-15 18:48 | +10 | ETH | UP | 0.55 | 0.70 | 1.17 |
| 10-15 18:48 | +5 | ETH | UP | 0.54 | 0.61 | 0.35 |
| 10-15 18:48 | +10 stop | XRP | DOWN | 0.65 | 0.49 | -1.94 |
| 10-15 18:48 | +15 | XRP | DOWN | 0.65 | open |  |
| 10-15 18:48 | +10 | XRP | DOWN | 0.65 | open |  |
| 10-15 18:48 | +5 | XRP | DOWN | 0.65 | open |  |
| 10-15 18:48 | +10 stop | NEAR | DOWN | 0.57 | 0.74 | 1.38 |
| 10-15 18:48 | +10 | NEAR | DOWN | 0.57 | 0.74 | 1.38 |
| 10-15 18:48 | +5 | NEAR | DOWN | 0.58 | 0.74 | 1.28 |
| 10-15 18:47 | +5 | SOL | DOWN | 0.42 | 0.56 | 1.04 |
| 10-15 18:47 | +5 | BTC | DOWN | 0.49 | 0.57 | 0.44 |
| 10-15 18:47 | +10 stop | ETH | DOWN | 0.47 | 0.57 | 0.64 |
| 10-15 18:47 | +20 | ETH | DOWN | 0.47 | open |  |
| 10-15 18:47 | +15 | ETH | DOWN | 0.47 | open |  |
| 10-15 18:47 | +10 | ETH | DOWN | 0.47 | 0.57 | 0.64 |
| 10-15 18:47 | +5 | ETH | DOWN | 0.47 | 0.57 | 0.64 |
| 10-15 18:47 | +10 stop | DOGE | DOWN | 0.65 | 0.50 | -1.84 |
| 10-15 18:47 | +20 | DOGE | DOWN | 0.65 | open |  |
