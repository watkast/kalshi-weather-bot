# Range-Scalp Bot

*Updated Tue Oct 06 01:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4439 | 3828 | 611 (6) | 0 | $-1491.95 | -5.3% |
| **+10¢** | 3417 | 2707 | 710 (9) | 1 | $-1385.53 | -6.4% |
| **+15¢** | 2865 | 2113 | 752 (12) | 3 | $-1223.64 | -6.8% |
| **+20¢** | 2567 | 1784 | 783 (17) | 3 | $-1031.07 | -6.4% |
| **+10¢ (15¢ stop)** | 5459 | 5448 | 11 (6) | 0 | $-1979.73 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 01:05 | +5 | BNB | UP | 0.62 | 0.74 | 0.89 |
| 10-06 01:04 | +10 stop | HYPE | UP | 0.61 | 0.74 | 0.99 |
| 10-06 01:04 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.74 |
| 10-06 01:04 | +20 | SOL | UP | 0.71 | 0.91 | 1.83 |
| 10-06 01:04 | +15 | SOL | UP | 0.71 | 0.86 | 1.26 |
| 10-06 01:04 | +10 | SOL | UP | 0.71 | 0.81 | 0.74 |
| 10-06 01:04 | +5 | SOL | UP | 0.71 | 0.81 | 0.74 |
| 10-06 01:04 | +10 stop | BNB | UP | 0.60 | 0.74 | 1.09 |
| 10-06 01:04 | +20 | BNB | UP | 0.60 | open |  |
| 10-06 01:04 | +15 | BNB | UP | 0.60 | open |  |
| 10-06 01:04 | +10 | BNB | UP | 0.60 | 0.74 | 1.09 |
| 10-06 01:04 | +5 | BNB | UP | 0.57 | 0.63 | 0.25 |
| 10-06 01:04 | +5 | ETH | UP | 0.55 | 0.62 | 0.35 |
| 10-06 01:03 | +10 stop | ETH | UP | 0.70 | 0.81 | 0.84 |
| 10-06 01:03 | +20 | ETH | UP | 0.70 | open |  |
| 10-06 01:03 | +15 | ETH | UP | 0.70 | open |  |
| 10-06 01:03 | +10 | ETH | UP | 0.70 | 0.81 | 0.84 |
| 10-06 01:03 | +5 | ETH | UP | 0.70 | 0.75 | 0.21 |
| 10-06 01:02 | +5 | NEAR | UP | 0.61 | 0.74 | 0.99 |
| 10-06 01:01 | +10 stop | NEAR | UP | 0.62 | 0.74 | 0.89 |
| 10-06 01:01 | +20 | NEAR | UP | 0.62 | 0.82 | 1.72 |
| 10-06 01:01 | +15 | NEAR | UP | 0.62 | 0.82 | 1.72 |
| 10-06 01:01 | +10 | NEAR | UP | 0.62 | 0.74 | 0.89 |
| 10-06 01:01 | +5 | NEAR | UP | 0.62 | 0.69 | 0.38 |
| 10-06 01:01 | +10 stop | HYPE | UP | 0.66 | 0.50 | -1.94 |
| 10-06 01:01 | +20 | HYPE | UP | 0.66 | open |  |
| 10-06 01:01 | +15 | HYPE | UP | 0.66 | open |  |
| 10-06 01:01 | +10 | HYPE | UP | 0.66 | open |  |
| 10-06 01:01 | +5 | HYPE | UP | 0.66 | 0.74 | 0.50 |
| 10-06 00:56 | +10 stop | ZEC | DOWN | 0.59 | 0.25 | -3.71 |
| 10-06 00:54 | +10 stop | ZEC | UP | 0.69 | 0.50 | -2.23 |
| 10-06 00:51 | +10 stop | DOGE | UP | 0.67 | 0.78 | 0.81 |
| 10-06 00:50 | +10 stop | BNB | UP | 0.57 | 0.30 | -3.03 |
| 10-06 00:50 | +10 stop | DOGE | UP | 0.70 | 0.52 | -2.13 |
| 10-06 00:49 | +10 stop | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 10-06 00:49 | +10 stop | NEAR | DOWN | 0.52 | 0.75 | 1.98 |
| 10-06 00:49 | +10 stop | ZEC | UP | 0.62 | 0.85 | 2.04 |
| 10-06 00:49 | +10 stop | BTC | UP | 0.58 | 0.74 | 1.28 |
| 10-06 00:49 | +10 stop | ETH | UP | 0.56 | 0.69 | 0.97 |
| 10-06 00:48 | +10 stop | ZEC | DOWN | 0.62 | 0.46 | -1.95 |
