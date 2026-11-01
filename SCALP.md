# Range-Scalp Bot

*Updated Sun Nov 01 03:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43129 | 37595 | 5534 (62) | 2 | $-12253.69 | -4.5% |
| **+10¢** | 32162 | 25768 | 6394 (84) | 3 | $-10975.61 | -5.4% |
| **+15¢** | 26908 | 20017 | 6891 (112) | 3 | $-10043.93 | -5.9% |
| **+20¢** | 23896 | 16676 | 7220 (146) | 3 | $-8876.64 | -5.9% |
| **+10¢ (15¢ stop)** | 52597 | 52514 | 83 (48) | 0 | $-19917.43 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 03:08 | +5 | NEAR | DOWN | 0.59 | open |  |
| 11-01 03:06 | +10 stop | BTC | UP | 0.66 | 0.78 | 0.91 |
| 11-01 03:06 | +5 | NEAR | DOWN | 0.59 | 0.65 | 0.27 |
| 11-01 03:05 | +5 | BNB | DOWN | 0.37 | 0.62 | 2.16 |
| 11-01 03:04 | +10 stop | ETH | UP | 0.69 | 0.89 | 1.78 |
| 11-01 03:04 | +10 | ETH | UP | 0.69 | 0.89 | 1.78 |
| 11-01 03:03 | +5 | ETH | UP | 0.68 | 0.76 | 0.49 |
| 11-01 03:02 | +10 stop | ETH | UP | 0.57 | 0.69 | 0.87 |
| 11-01 03:02 | +20 | ETH | UP | 0.57 | 0.89 | 2.95 |
| 11-01 03:02 | +15 | ETH | UP | 0.57 | 0.72 | 1.17 |
| 11-01 03:02 | +10 | ETH | UP | 0.56 | 0.69 | 0.97 |
| 11-01 03:02 | +5 | ETH | UP | 0.56 | 0.61 | 0.15 |
| 11-01 03:02 | +5 | ZEC | UP | 0.64 | 0.70 | 0.28 |
| 11-01 03:02 | +5 | SOL | UP | 0.67 | 0.72 | 0.19 |
| 11-01 03:01 | +10 stop | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 11-01 03:01 | +20 | HYPE | UP | 0.66 | 0.86 | 1.75 |
| 11-01 03:01 | +15 | HYPE | UP | 0.66 | 0.86 | 1.75 |
| 11-01 03:01 | +10 | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 11-01 03:01 | +5 | HYPE | UP | 0.66 | 0.72 | 0.29 |
| 11-01 03:01 | +10 stop | DOGE | UP | 0.59 | 0.71 | 0.85 |
| 11-01 03:01 | +20 | DOGE | UP | 0.59 | 0.81 | 1.89 |
| 11-01 03:01 | +15 | DOGE | UP | 0.59 | 0.78 | 1.57 |
| 11-01 03:01 | +10 | DOGE | UP | 0.59 | 0.71 | 0.85 |
| 11-01 03:01 | +5 | DOGE | UP | 0.59 | 0.69 | 0.65 |
| 11-01 03:01 | +10 stop | BNB | DOWN | 0.55 | 0.38 | -2.05 |
| 11-01 03:01 | +20 | BNB | DOWN | 0.55 | open |  |
| 11-01 03:01 | +15 | BNB | DOWN | 0.55 | open |  |
| 11-01 03:01 | +10 | BNB | DOWN | 0.55 | open |  |
| 11-01 03:01 | +5 | BNB | DOWN | 0.55 | 0.60 | 0.15 |
| 11-01 03:01 | +10 stop | BTC | DOWN | 0.62 | 0.43 | -2.25 |
| 11-01 03:01 | +20 | BTC | DOWN | 0.62 | open |  |
| 11-01 03:01 | +15 | BTC | DOWN | 0.62 | open |  |
| 11-01 03:01 | +10 | BTC | DOWN | 0.62 | open |  |
| 11-01 03:01 | +5 | BTC | DOWN | 0.62 | open |  |
| 11-01 03:01 | +10 stop | XRP | UP | 0.65 | 0.77 | 0.91 |
| 11-01 03:01 | +20 | XRP | UP | 0.65 | 0.88 | 2.06 |
| 11-01 03:01 | +15 | XRP | UP | 0.65 | 0.82 | 1.43 |
| 11-01 03:01 | +10 | XRP | UP | 0.65 | 0.77 | 0.91 |
| 11-01 03:01 | +5 | XRP | UP | 0.65 | 0.71 | 0.29 |
| 11-01 03:01 | +10 stop | ZEC | UP | 0.60 | 0.70 | 0.68 |
