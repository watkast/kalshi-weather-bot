# Range-Scalp Bot

*Updated Sun Oct 25 17:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33443 | 29179 | 4264 (42) | 4 | $-9394.72 | -4.5% |
| **+10¢** | 25034 | 20101 | 4933 (60) | 4 | $-8339.02 | -5.3% |
| **+15¢** | 20942 | 15631 | 5311 (83) | 4 | $-7511.44 | -5.7% |
| **+20¢** | 18558 | 12997 | 5561 (105) | 4 | $-6617.17 | -5.7% |
| **+10¢ (15¢ stop)** | 41000 | 40940 | 60 (32) | 1 | $-15640.35 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 17:10 | +10 stop | BTC | DOWN | 0.64 | open |  |
| 10-25 17:08 | +10 stop | HYPE | UP | 0.59 | 0.22 | -4.04 |
| 10-25 17:08 | +10 stop | DOGE | DOWN | 0.70 | 0.83 | 1.05 |
| 10-25 17:08 | +5 | SOL | DOWN | 0.57 | 0.70 | 0.97 |
| 10-25 17:08 | +10 stop | HYPE | UP | 0.71 | 0.55 | -1.93 |
| 10-25 17:08 | +10 | HYPE | UP | 0.71 | open |  |
| 10-25 17:08 | +5 | HYPE | UP | 0.71 | open |  |
| 10-25 17:07 | +10 stop | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 10-25 17:07 | +10 | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 10-25 17:07 | +5 | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 10-25 17:07 | +10 stop | BTC | DOWN | 0.58 | 0.39 | -2.25 |
| 10-25 17:07 | +10 stop | NEAR | UP | 0.62 | 0.76 | 1.10 |
| 10-25 17:07 | +10 stop | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 10-25 17:07 | +10 stop | HYPE | UP | 0.55 | 0.67 | 0.86 |
| 10-25 17:07 | +15 | HYPE | UP | 0.55 | open |  |
| 10-25 17:07 | +10 | HYPE | UP | 0.55 | 0.67 | 0.86 |
| 10-25 17:07 | +5 | HYPE | UP | 0.55 | 0.67 | 0.86 |
| 10-25 17:06 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-25 17:06 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-25 17:06 | +20 | XRP | DOWN | 0.68 | 0.88 | 1.77 |
| 10-25 17:06 | +15 | XRP | DOWN | 0.68 | 0.87 | 1.66 |
| 10-25 17:06 | +10 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-25 17:06 | +5 | XRP | DOWN | 0.68 | 0.75 | 0.40 |
| 10-25 17:06 | +10 stop | ZEC | UP | 0.66 | 0.77 | 0.81 |
| 10-25 17:06 | +10 stop | DOGE | UP | 0.54 | 0.36 | -2.15 |
| 10-25 17:06 | +10 stop | BTC | UP | 0.57 | 0.38 | -2.25 |
| 10-25 17:06 | +10 stop | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 10-25 17:06 | +20 | ETH | DOWN | 0.60 | 0.85 | 2.24 |
| 10-25 17:06 | +15 | ETH | DOWN | 0.60 | 0.75 | 1.19 |
| 10-25 17:06 | +10 | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 10-25 17:06 | +5 | ETH | DOWN | 0.60 | 0.67 | 0.37 |
| 10-25 17:05 | +10 stop | DOGE | DOWN | 0.69 | 0.45 | -2.73 |
| 10-25 17:05 | +20 | DOGE | DOWN | 0.69 | 0.89 | 1.78 |
| 10-25 17:05 | +15 | DOGE | DOWN | 0.69 | 0.89 | 1.78 |
| 10-25 17:05 | +10 | DOGE | DOWN | 0.69 | 0.83 | 1.15 |
| 10-25 17:05 | +5 | DOGE | DOWN | 0.69 | 0.75 | 0.31 |
| 10-25 17:05 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 10-25 17:05 | +5 | HYPE | UP | 0.60 | 0.72 | 0.88 |
| 10-25 17:05 | +10 stop | HYPE | UP | 0.61 | 0.72 | 0.80 |
| 10-25 17:04 | +10 stop | BNB | DOWN | 0.70 | 0.48 | -2.53 |
