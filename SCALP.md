# Range-Scalp Bot

*Updated Sat Oct 03 07:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 413 | 352 | 61 (1) | 3 | $-167.06 | -6.3% |
| **+10¢** | 330 | 264 | 66 (2) | 3 | $-112.86 | -5.4% |
| **+15¢** | 276 | 206 | 70 (2) | 3 | $-116.49 | -6.7% |
| **+20¢** | 238 | 165 | 73 (2) | 4 | $-115.72 | -7.7% |
| **+10¢ (15¢ stop)** | 556 | 555 | 1 (1) | 3 | $-271.31 | -7.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 07:47 | +10 stop | SOL | UP | 0.69 | open |  |
| 10-03 07:47 | +10 stop | HYPE | UP | 0.67 | open |  |
| 10-03 07:47 | +20 | HYPE | UP | 0.67 | open |  |
| 10-03 07:47 | +15 | HYPE | UP | 0.70 | open |  |
| 10-03 07:47 | +10 | HYPE | UP | 0.70 | open |  |
| 10-03 07:47 | +5 | HYPE | UP | 0.70 | open |  |
| 10-03 07:47 | +10 stop | ETH | UP | 0.67 | open |  |
| 10-03 07:47 | +20 | ETH | UP | 0.67 | open |  |
| 10-03 07:47 | +15 | ETH | UP | 0.67 | open |  |
| 10-03 07:47 | +10 | ETH | UP | 0.67 | open |  |
| 10-03 07:47 | +5 | ETH | UP | 0.67 | open |  |
| 10-03 07:46 | +10 stop | NEAR | UP | 0.62 | 0.78 | 1.30 |
| 10-03 07:46 | +20 | NEAR | UP | 0.62 | open |  |
| 10-03 07:46 | +15 | NEAR | UP | 0.62 | 0.78 | 1.30 |
| 10-03 07:46 | +10 | NEAR | UP | 0.62 | 0.78 | 1.30 |
| 10-03 07:46 | +5 | NEAR | UP | 0.62 | 0.78 | 1.30 |
| 10-03 07:46 | +10 stop | SOL | DOWN | 0.55 | 0.30 | -2.83 |
| 10-03 07:46 | +20 | SOL | DOWN | 0.55 | open |  |
| 10-03 07:46 | +15 | SOL | DOWN | 0.55 | open |  |
| 10-03 07:46 | +10 | SOL | DOWN | 0.55 | open |  |
| 10-03 07:46 | +5 | SOL | DOWN | 0.55 | open |  |
| 10-03 07:46 | +10 stop | DOGE | UP | 0.56 | 0.76 | 1.74 |
| 10-03 07:46 | +20 | DOGE | UP | 0.56 | 0.76 | 1.69 |
| 10-03 07:46 | +15 | DOGE | UP | 0.56 | 0.76 | 1.64 |
| 10-03 07:46 | +10 | DOGE | UP | 0.56 | 0.76 | 1.74 |
| 10-03 07:46 | +5 | DOGE | UP | 0.56 | 0.76 | 1.64 |
| 10-03 07:42 | +10 stop | HYPE | DOWN | 0.69 | no | 2.95 |
| 10-03 07:42 | +20 | HYPE | DOWN | 0.69 | no | 2.95 |
| 10-03 07:42 | +15 | HYPE | DOWN | 0.69 | no | 2.95 |
| 10-03 07:42 | +10 | HYPE | DOWN | 0.69 | no | 2.95 |
| 10-03 07:42 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-03 07:42 | +10 stop | ETH | UP | 0.69 | 0.48 | -2.43 |
| 10-03 07:42 | +20 | ETH | UP | 0.69 | 0.93 | 2.22 |
| 10-03 07:42 | +15 | ETH | UP | 0.69 | 0.93 | 2.22 |
| 10-03 07:42 | +10 | ETH | UP | 0.69 | 0.93 | 2.22 |
| 10-03 07:42 | +5 | ETH | UP | 0.69 | 0.93 | 2.22 |
| 10-03 07:42 | +10 stop | BTC | DOWN | 0.65 | 0.92 | 2.47 |
| 10-03 07:40 | +10 stop | BNB | UP | 0.57 | 0.18 | -4.19 |
| 10-03 07:40 | +10 stop | BTC | UP | 0.69 | 0.39 | -3.32 |
| 10-03 07:40 | +15 | BTC | UP | 0.69 | no | -7.05 |
