# Range-Scalp Bot

*Updated Sat Oct 03 11:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 718 | 624 | 94 (1) | 2 | $-213.38 | -4.7% |
| **+10¢** | 549 | 445 | 104 (2) | 2 | $-154.59 | -4.5% |
| **+15¢** | 464 | 353 | 111 (3) | 3 | $-132.09 | -4.5% |
| **+20¢** | 402 | 287 | 115 (3) | 5 | $-119.42 | -4.7% |
| **+10¢ (15¢ stop)** | 926 | 925 | 1 (1) | 1 | $-495.88 | -8.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 11:58 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 10-03 11:57 | +10 stop | BNB | DOWN | 0.69 | 0.54 | -1.83 |
| 10-03 11:56 | +5 | ZEC | UP | 0.61 | open |  |
| 10-03 11:56 | +10 stop | ZEC | UP | 0.62 | 0.01 | -6.33 |
| 10-03 11:54 | +10 stop | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 10-03 11:54 | +10 stop | DOGE | UP | 0.67 | 0.77 | 0.76 |
| 10-03 11:54 | +20 | DOGE | UP | 0.67 | open |  |
| 10-03 11:54 | +15 | DOGE | UP | 0.67 | open |  |
| 10-03 11:54 | +10 | DOGE | UP | 0.67 | 0.77 | 0.74 |
| 10-03 11:54 | +5 | DOGE | UP | 0.67 | 0.77 | 0.74 |
| 10-03 11:54 | +10 stop | XRP | UP | 0.59 | 0.70 | 0.78 |
| 10-03 11:54 | +10 | XRP | UP | 0.59 | 0.70 | 0.78 |
| 10-03 11:54 | +5 | XRP | UP | 0.61 | 0.68 | 0.37 |
| 10-03 11:54 | +10 stop | HYPE | UP | 0.65 | 0.78 | 1.01 |
| 10-03 11:54 | +20 | HYPE | UP | 0.65 | 0.93 | 2.57 |
| 10-03 11:54 | +15 | HYPE | UP | 0.65 | 0.93 | 2.57 |
| 10-03 11:54 | +10 | HYPE | UP | 0.65 | 0.78 | 1.01 |
| 10-03 11:54 | +5 | HYPE | UP | 0.65 | 0.78 | 1.01 |
| 10-03 11:53 | +5 | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-03 11:51 | +10 stop | ZEC | DOWN | 0.53 | 0.37 | -1.92 |
| 10-03 11:51 | +5 | SOL | UP | 0.61 | 0.68 | 0.37 |
| 10-03 11:50 | +10 stop | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 10-03 11:50 | +10 | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 10-03 11:50 | +5 | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 10-03 11:50 | +10 stop | BNB | DOWN | 0.59 | 0.42 | -2.05 |
| 10-03 11:50 | +10 | BNB | DOWN | 0.58 | 0.70 | 0.87 |
| 10-03 11:50 | +5 | BNB | DOWN | 0.58 | 0.66 | 0.46 |
| 10-03 11:50 | +10 stop | SOL | UP | 0.69 | 0.79 | 0.73 |
| 10-03 11:50 | +10 | SOL | UP | 0.69 | 0.79 | 0.73 |
| 10-03 11:50 | +5 | SOL | UP | 0.69 | 0.74 | 0.21 |
| 10-03 11:50 | +10 stop | XRP | UP | 0.68 | 0.51 | -2.04 |
| 10-03 11:50 | +15 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 10-03 11:50 | +10 | XRP | UP | 0.68 | 0.78 | 0.71 |
| 10-03 11:50 | +5 | XRP | UP | 0.68 | 0.73 | 0.20 |
| 10-03 11:49 | +10 stop | ZEC | UP | 0.61 | 0.44 | -2.05 |
| 10-03 11:49 | +10 | ZEC | UP | 0.61 | open |  |
| 10-03 11:49 | +5 | ZEC | UP | 0.61 | 0.67 | 0.27 |
| 10-03 11:49 | +5 | ETH | UP | 0.60 | open |  |
| 10-03 11:46 | +10 stop | BTC | UP | 0.71 | 0.53 | -2.13 |
| 10-03 11:46 | +20 | BTC | UP | 0.71 | 0.91 | 1.81 |
