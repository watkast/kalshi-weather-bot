# Range-Scalp Bot

*Updated Tue Oct 27 21:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37081 | 32379 | 4702 (45) | 2 | $-10271.08 | -4.4% |
| **+10¢** | 27696 | 22248 | 5448 (67) | 3 | $-9151.94 | -5.3% |
| **+15¢** | 23168 | 17319 | 5849 (91) | 4 | $-8099.69 | -5.6% |
| **+20¢** | 20528 | 14408 | 6120 (116) | 4 | $-7058.67 | -5.5% |
| **+10¢ (15¢ stop)** | 45424 | 45359 | 65 (34) | 1 | $-17292.46 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 21:11 | +10 stop | ETH | UP | 0.41 | 0.53 | 0.85 |
| 10-27 21:11 | +15 | ETH | UP | 0.41 | open |  |
| 10-27 21:11 | +10 | ETH | UP | 0.41 | 0.53 | 0.85 |
| 10-27 21:11 | +5 | ETH | UP | 0.41 | 0.53 | 0.85 |
| 10-27 21:10 | +10 stop | XRP | DOWN | 0.62 | open |  |
| 10-27 21:09 | +10 stop | NEAR | UP | 0.54 | 0.29 | -2.83 |
| 10-27 21:09 | +10 | NEAR | UP | 0.54 | open |  |
| 10-27 21:09 | +5 | NEAR | UP | 0.54 | 0.59 | 0.15 |
| 10-27 21:08 | +10 stop | XRP | UP | 0.60 | 0.27 | -3.61 |
| 10-27 21:08 | +10 stop | ETH | UP | 0.65 | 0.78 | 1.01 |
| 10-27 21:06 | +10 stop | DOGE | UP | 0.70 | 0.83 | 1.05 |
| 10-27 21:06 | +5 | ZEC | UP | 0.62 | 0.72 | 0.68 |
| 10-27 21:06 | +15 | ZEC | UP | 0.65 | 0.84 | 1.64 |
| 10-27 21:06 | +10 stop | ZEC | UP | 0.65 | 0.77 | 0.91 |
| 10-27 21:06 | +10 | ZEC | UP | 0.65 | 0.77 | 0.91 |
| 10-27 21:06 | +5 | ZEC | UP | 0.64 | 0.69 | 0.18 |
| 10-27 21:05 | +10 stop | ETH | DOWN | 0.53 | 0.35 | -2.14 |
| 10-27 21:05 | +10 stop | XRP | DOWN | 0.66 | 0.40 | -2.93 |
| 10-27 21:05 | +10 stop | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 10-27 21:04 | +10 stop | DOGE | UP | 0.53 | 0.65 | 0.86 |
| 10-27 21:04 | +10 stop | BTC | DOWN | 0.49 | 0.66 | 1.36 |
| 10-27 21:03 | +10 stop | HYPE | UP | 0.64 | 0.79 | 1.21 |
| 10-27 21:03 | +20 | HYPE | UP | 0.64 | 0.84 | 1.73 |
| 10-27 21:03 | +15 | HYPE | UP | 0.64 | 0.79 | 1.21 |
| 10-27 21:03 | +10 | HYPE | UP | 0.64 | 0.79 | 1.21 |
| 10-27 21:03 | +5 | HYPE | UP | 0.64 | 0.79 | 1.21 |
| 10-27 21:02 | +10 stop | BNB | UP | 0.69 | 0.79 | 0.73 |
| 10-27 21:02 | +20 | BNB | UP | 0.69 | 0.92 | 2.10 |
| 10-27 21:02 | +15 | BNB | UP | 0.69 | 0.87 | 1.57 |
| 10-27 21:02 | +10 | BNB | UP | 0.69 | 0.79 | 0.73 |
| 10-27 21:02 | +5 | BNB | UP | 0.69 | 0.74 | 0.21 |
| 10-27 21:02 | +10 stop | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 10-27 21:02 | +20 | NEAR | UP | 0.70 | open |  |
| 10-27 21:02 | +15 | NEAR | UP | 0.70 | open |  |
| 10-27 21:02 | +10 | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 10-27 21:02 | +5 | NEAR | UP | 0.70 | 0.78 | 0.52 |
| 10-27 21:02 | +10 stop | ETH | UP | 0.65 | 0.48 | -2.04 |
| 10-27 21:02 | +20 | ETH | UP | 0.65 | open |  |
| 10-27 21:02 | +15 | ETH | UP | 0.65 | 0.81 | 1.33 |
| 10-27 21:02 | +10 | ETH | UP | 0.65 | 0.78 | 1.01 |
