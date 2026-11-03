# Range-Scalp Bot

*Updated Tue Nov 03 14:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46035 | 40081 | 5954 (70) | 3 | $-13294.43 | -4.6% |
| **+10¢** | 34367 | 27471 | 6896 (92) | 4 | $-12150.74 | -5.6% |
| **+15¢** | 28763 | 21348 | 7415 (120) | 4 | $-11094.79 | -6.1% |
| **+20¢** | 25549 | 17778 | 7771 (157) | 4 | $-9859.30 | -6.2% |
| **+10¢ (15¢ stop)** | 56159 | 56070 | 89 (53) | 4 | $-21042.76 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 14:01 | +5 | ETH | DOWN | 0.59 | open |  |
| 11-03 14:01 | +5 | BTC | DOWN | 0.60 | open |  |
| 11-03 14:00 | +10 stop | ETH | DOWN | 0.53 | open |  |
| 11-03 14:00 | +20 | ETH | DOWN | 0.53 | open |  |
| 11-03 14:00 | +15 | ETH | DOWN | 0.53 | open |  |
| 11-03 14:00 | +10 | ETH | DOWN | 0.53 | open |  |
| 11-03 14:00 | +5 | ETH | DOWN | 0.53 | 0.58 | 0.14 |
| 11-03 14:00 | +10 stop | BNB | DOWN | 0.62 | open |  |
| 11-03 14:00 | +20 | BNB | DOWN | 0.62 | open |  |
| 11-03 14:00 | +15 | BNB | DOWN | 0.62 | open |  |
| 11-03 14:00 | +10 | BNB | DOWN | 0.62 | open |  |
| 11-03 14:00 | +5 | BNB | DOWN | 0.62 | open |  |
| 11-03 14:00 | +10 stop | BTC | DOWN | 0.55 | open |  |
| 11-03 14:00 | +20 | BTC | DOWN | 0.55 | open |  |
| 11-03 14:00 | +15 | BTC | DOWN | 0.55 | open |  |
| 11-03 14:00 | +10 | BTC | DOWN | 0.55 | open |  |
| 11-03 14:00 | +5 | BTC | DOWN | 0.55 | 0.61 | 0.25 |
| 11-03 14:00 | +10 stop | SOL | DOWN | 0.49 | open |  |
| 11-03 14:00 | +20 | SOL | DOWN | 0.49 | open |  |
| 11-03 14:00 | +15 | SOL | DOWN | 0.49 | open |  |
| 11-03 14:00 | +10 | SOL | DOWN | 0.49 | open |  |
| 11-03 14:00 | +5 | SOL | DOWN | 0.49 | 0.55 | 0.24 |
| 11-03 13:59 | +10 stop | NEAR | UP | 0.37 | 0.53 | 1.25 |
| 11-03 13:58 | +10 stop | XRP | UP | 0.66 | 0.94 | 2.64 |
| 11-03 13:57 | +10 stop | XRP | DOWN | 0.59 | 0.37 | -2.54 |
| 11-03 13:56 | +10 stop | XRP | UP | 0.51 | 0.35 | -1.94 |
| 11-03 13:55 | +5 | XRP | UP | 0.61 | 0.75 | 1.09 |
| 11-03 13:53 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.06 |
| 11-03 13:52 | +10 stop | XRP | UP | 0.70 | 0.54 | -1.93 |
| 11-03 13:52 | +20 | XRP | UP | 0.70 | 0.94 | 2.25 |
| 11-03 13:52 | +15 | XRP | UP | 0.70 | 0.94 | 2.25 |
| 11-03 13:52 | +10 | XRP | UP | 0.70 | 0.94 | 2.25 |
| 11-03 13:52 | +5 | XRP | UP | 0.70 | 0.75 | 0.21 |
| 11-03 13:51 | +10 stop | HYPE | DOWN | 0.65 | 0.83 | 1.50 |
| 11-03 13:51 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-03 13:51 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-03 13:50 | +10 stop | HYPE | UP | 0.54 | 0.36 | -2.15 |
| 11-03 13:50 | +10 stop | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-03 13:50 | +10 stop | SOL | UP | 0.69 | 0.54 | -1.83 |
| 11-03 13:50 | +10 stop | DOGE | UP | 0.64 | 0.45 | -2.25 |
