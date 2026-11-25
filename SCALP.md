# Range-Scalp Bot

*Updated Wed Nov 25 19:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71979 | 62823 | 9156 (158) | 4 | $-19184.61 | -4.2% |
| **+10¢** | 53705 | 43013 | 10692 (203) | 5 | $-17773.53 | -5.3% |
| **+15¢** | 44969 | 33452 | 11517 (260) | 7 | $-15868.37 | -5.6% |
| **+20¢** | 40037 | 27907 | 12130 (326) | 9 | $-14270.84 | -5.7% |
| **+10¢ (15¢ stop)** | 87632 | 87423 | 209 (128) | 4 | $-32132.92 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 19:37 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 11-25 19:37 | +10 | ZEC | DOWN | 0.71 | open |  |
| 11-25 19:37 | +10 stop | XRP | DOWN | 0.59 | open |  |
| 11-25 19:37 | +10 | XRP | DOWN | 0.59 | open |  |
| 11-25 19:37 | +5 | XRP | DOWN | 0.57 | open |  |
| 11-25 19:35 | +10 stop | XRP | DOWN | 0.52 | 0.66 | 1.06 |
| 11-25 19:35 | +10 | XRP | DOWN | 0.53 | 0.66 | 0.96 |
| 11-25 19:35 | +5 | XRP | DOWN | 0.52 | 0.66 | 1.06 |
| 11-25 19:35 | +10 stop | ZEC | DOWN | 0.70 | 0.46 | -2.73 |
| 11-25 19:35 | +5 | ZEC | DOWN | 0.71 | open |  |
| 11-25 19:35 | +10 stop | DOGE | DOWN | 0.69 | open |  |
| 11-25 19:35 | +20 | DOGE | DOWN | 0.69 | open |  |
| 11-25 19:35 | +15 | DOGE | DOWN | 0.69 | open |  |
| 11-25 19:35 | +10 | DOGE | DOWN | 0.69 | open |  |
| 11-25 19:35 | +5 | DOGE | DOWN | 0.69 | open |  |
| 11-25 19:34 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-25 19:34 | +10 stop | ZEC | DOWN | 0.55 | 0.65 | 0.68 |
| 11-25 19:33 | +10 stop | BTC | DOWN | 0.59 | 0.75 | 1.29 |
| 11-25 19:33 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-25 19:33 | +10 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-25 19:33 | +5 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-25 19:33 | +10 stop | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 11-25 19:33 | +10 | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 11-25 19:33 | +5 | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 11-25 19:33 | +10 stop | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 11-25 19:33 | +20 | HYPE | DOWN | 0.55 | open |  |
| 11-25 19:33 | +15 | HYPE | DOWN | 0.55 | 0.71 | 1.27 |
| 11-25 19:33 | +10 | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-25 19:33 | +5 | HYPE | DOWN | 0.57 | 0.62 | 0.15 |
| 11-25 19:33 | +10 stop | ETH | DOWN | 0.63 | open |  |
| 11-25 19:32 | +10 stop | XRP | DOWN | 0.60 | 0.73 | 0.99 |
| 11-25 19:32 | +20 | XRP | DOWN | 0.60 | open |  |
| 11-25 19:32 | +15 | XRP | DOWN | 0.61 | open |  |
| 11-25 19:32 | +10 | XRP | DOWN | 0.61 | 0.73 | 0.92 |
| 11-25 19:32 | +5 | XRP | DOWN | 0.61 | 0.73 | 0.88 |
| 11-25 19:32 | +10 stop | NEAR | UP | 0.67 | 0.78 | 0.83 |
| 11-25 19:32 | +20 | NEAR | UP | 0.64 | open |  |
| 11-25 19:32 | +15 | NEAR | UP | 0.64 | 0.83 | 1.63 |
| 11-25 19:32 | +10 | NEAR | UP | 0.64 | 0.78 | 1.10 |
| 11-25 19:32 | +5 | NEAR | UP | 0.64 | 0.71 | 0.38 |
