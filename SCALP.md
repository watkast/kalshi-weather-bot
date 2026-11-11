# Range-Scalp Bot

*Updated Wed Nov 11 14:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55983 | 48816 | 7167 (94) | 2 | $-15341.80 | -4.4% |
| **+10¢** | 41827 | 33468 | 8359 (124) | 3 | $-14291.91 | -5.4% |
| **+15¢** | 35073 | 26057 | 9016 (158) | 1 | $-13046.87 | -5.9% |
| **+20¢** | 31240 | 21782 | 9458 (208) | 1 | $-11420.26 | -5.8% |
| **+10¢ (15¢ stop)** | 68211 | 68090 | 121 (73) | 0 | $-25132.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 14:57 | +10 stop | XRP | UP | 0.50 | 0.61 | 0.75 |
| 11-11 14:57 | +10 | XRP | UP | 0.50 | 0.61 | 0.75 |
| 11-11 14:57 | +5 | XRP | UP | 0.50 | 0.57 | 0.34 |
| 11-11 14:56 | +10 stop | DOGE | DOWN | 0.71 | 0.47 | -2.73 |
| 11-11 14:56 | +20 | DOGE | DOWN | 0.69 | 0.92 | 2.10 |
| 11-11 14:56 | +15 | DOGE | DOWN | 0.69 | 0.92 | 2.10 |
| 11-11 14:56 | +10 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-11 14:56 | +5 | DOGE | DOWN | 0.69 | 0.78 | 0.62 |
| 11-11 14:56 | +10 stop | BTC | UP | 0.57 | 0.34 | -2.64 |
| 11-11 14:56 | +10 | BTC | UP | 0.54 | open |  |
| 11-11 14:55 | +5 | BTC | DOWN | 0.71 | 0.96 | 2.35 |
| 11-11 14:55 | +10 stop | ETH | DOWN | 0.59 | 0.23 | -3.90 |
| 11-11 14:55 | +10 | ETH | DOWN | 0.59 | open |  |
| 11-11 14:55 | +5 | ETH | DOWN | 0.59 | open |  |
| 11-11 14:54 | +5 | BNB | DOWN | 0.69 | open |  |
| 11-11 14:54 | +10 stop | BNB | DOWN | 0.69 | 0.51 | -2.13 |
| 11-11 14:54 | +10 stop | XRP | DOWN | 0.60 | 0.24 | -3.90 |
| 11-11 14:54 | +10 stop | BTC | DOWN | 0.67 | 0.40 | -3.03 |
| 11-11 14:53 | +10 stop | ETH | UP | 0.53 | 0.64 | 0.78 |
| 11-11 14:53 | +10 | ETH | UP | 0.53 | 0.64 | 0.78 |
| 11-11 14:53 | +5 | ETH | UP | 0.53 | 0.64 | 0.78 |
| 11-11 14:53 | +10 stop | BTC | UP | 0.43 | 0.59 | 1.25 |
| 11-11 14:53 | +5 | XRP | UP | 0.59 | 0.75 | 1.29 |
| 11-11 14:53 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-11 14:53 | +10 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-11 14:53 | +5 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-11 14:53 | +10 stop | BNB | UP | 0.58 | 0.43 | -1.86 |
| 11-11 14:53 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-11 14:53 | +10 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-11 14:53 | +5 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-11 14:52 | +10 stop | XRP | UP | 0.61 | 0.45 | -1.95 |
| 11-11 14:52 | +10 | XRP | UP | 0.61 | 0.75 | 1.09 |
| 11-11 14:52 | +5 | XRP | UP | 0.61 | 0.67 | 0.27 |
| 11-11 14:52 | +10 stop | DOGE | DOWN | 0.51 | 0.74 | 1.98 |
| 11-11 14:52 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-11 14:52 | +10 stop | NEAR | DOWN | 0.56 | 0.73 | 1.38 |
| 11-11 14:51 | +10 stop | BNB | UP | 0.67 | 0.50 | -2.04 |
| 11-11 14:50 | +10 stop | DOGE | DOWN | 0.56 | 0.41 | -1.85 |
| 11-11 14:50 | +10 stop | SOL | DOWN | 0.66 | 0.49 | -2.04 |
| 11-11 14:50 | +5 | SOL | DOWN | 0.66 | 0.71 | 0.19 |
