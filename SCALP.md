# Range-Scalp Bot

*Updated Wed Oct 21 07:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26837 | 23371 | 3466 (33) | 4 | $-7848.43 | -4.6% |
| **+10¢** | 20195 | 16189 | 4006 (48) | 4 | $-6955.64 | -5.5% |
| **+15¢** | 16908 | 12602 | 4306 (72) | 4 | $-6167.04 | -5.8% |
| **+20¢** | 14971 | 10456 | 4515 (91) | 4 | $-5544.77 | -5.9% |
| **+10¢ (15¢ stop)** | 32915 | 32862 | 53 (30) | 0 | $-12152.09 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 06:56 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-21 06:55 | +5 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-21 06:55 | +5 | DOGE | UP | 0.67 | 0.75 | 0.50 |
| 10-21 06:55 | +10 stop | XRP | DOWN | 0.62 | 0.81 | 1.62 |
| 10-21 06:55 | +10 stop | BNB | UP | 0.60 | 0.35 | -2.83 |
| 10-21 06:55 | +10 stop | DOGE | UP | 0.59 | 0.43 | -1.95 |
| 10-21 06:55 | +10 | DOGE | UP | 0.59 | 0.70 | 0.78 |
| 10-21 06:55 | +5 | DOGE | UP | 0.59 | 0.66 | 0.37 |
| 10-21 06:54 | +10 stop | HYPE | UP | 0.67 | 0.48 | -2.28 |
| 10-21 06:53 | +10 stop | BNB | DOWN | 0.61 | 0.39 | -2.54 |
| 10-21 06:53 | +5 | NEAR | UP | 0.66 | 0.78 | 0.91 |
| 10-21 06:53 | +10 stop | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 10-21 06:53 | +5 | DOGE | UP | 0.58 | 0.69 | 0.75 |
| 10-21 06:53 | +10 stop | DOGE | UP | 0.48 | 0.65 | 1.36 |
| 10-21 06:52 | +10 stop | BNB | UP | 0.64 | 0.45 | -2.25 |
| 10-21 06:52 | +10 stop | HYPE | UP | 0.70 | 0.55 | -1.83 |
| 10-21 06:52 | +5 | HYPE | UP | 0.70 | 0.75 | 0.21 |
| 10-21 06:52 | +10 stop | DOGE | DOWN | 0.57 | 0.40 | -2.02 |
| 10-21 06:51 | +10 stop | NEAR | UP | 0.59 | 0.78 | 1.60 |
| 10-21 06:51 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-21 06:50 | +10 stop | BNB | DOWN | 0.62 | 0.47 | -1.85 |
| 10-21 06:50 | +10 stop | BTC | DOWN | 0.69 | 0.83 | 1.15 |
| 10-21 06:50 | +10 stop | SOL | DOWN | 0.59 | 0.70 | 0.78 |
| 10-21 06:50 | +10 stop | NEAR | DOWN | 0.54 | 0.39 | -1.85 |
| 10-21 06:49 | +5 | DOGE | UP | 0.59 | 0.65 | 0.27 |
| 10-21 06:49 | +5 | HYPE | UP | 0.68 | 0.82 | 1.09 |
| 10-21 06:49 | +5 | ETH | DOWN | 0.63 | 0.71 | 0.48 |
| 10-21 06:49 | +10 stop | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 10-21 06:49 | +10 | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 10-21 06:49 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 10-21 06:48 | +10 stop | BNB | UP | 0.63 | 0.48 | -1.85 |
| 10-21 06:48 | +20 | BNB | UP | 0.63 | open |  |
| 10-21 06:48 | +15 | BNB | UP | 0.63 | open |  |
| 10-21 06:48 | +10 | BNB | UP | 0.63 | open |  |
| 10-21 06:48 | +5 | BNB | UP | 0.63 | open |  |
| 10-21 06:48 | +5 | DOGE | UP | 0.60 | 0.65 | 0.17 |
| 10-21 06:48 | +10 stop | ETH | DOWN | 0.56 | 0.66 | 0.66 |
| 10-21 06:48 | +20 | ETH | DOWN | 0.56 | 0.76 | 1.69 |
| 10-21 06:48 | +15 | ETH | DOWN | 0.56 | 0.71 | 1.17 |
| 10-21 06:48 | +10 | ETH | DOWN | 0.56 | 0.66 | 0.66 |
