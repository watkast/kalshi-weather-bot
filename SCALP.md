# Range-Scalp Bot

*Updated Fri Nov 27 17:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73839 | 64444 | 9395 (171) | 1 | $-19608.36 | -4.2% |
| **+10¢** | 55022 | 44049 | 10973 (216) | 1 | $-18237.08 | -5.3% |
| **+15¢** | 46075 | 34256 | 11819 (274) | 1 | $-16320.14 | -5.6% |
| **+20¢** | 41001 | 28551 | 12450 (341) | 1 | $-14753.28 | -5.7% |
| **+10¢ (15¢ stop)** | 89915 | 89696 | 219 (135) | 1 | $-33283.13 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 17:37 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.76 |
| 11-27 17:37 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.24 |
| 11-27 17:36 | +10 stop | SOL | DOWN | 0.69 | 0.82 | 1.05 |
| 11-27 17:36 | +10 stop | BTC | DOWN | 0.64 | open |  |
| 11-27 17:35 | +10 stop | HYPE | UP | 0.60 | 0.45 | -1.85 |
| 11-27 17:35 | +10 stop | BTC | UP | 0.62 | 0.45 | -2.05 |
| 11-27 17:35 | +10 stop | SOL | UP | 0.62 | 0.40 | -2.54 |
| 11-27 17:35 | +10 stop | BNB | UP | 0.65 | 0.42 | -2.64 |
| 11-27 17:34 | +10 stop | BTC | UP | 0.52 | 0.62 | 0.65 |
| 11-27 17:34 | +10 stop | NEAR | DOWN | 0.69 | 0.51 | -2.09 |
| 11-27 17:34 | +20 | NEAR | DOWN | 0.69 | 0.89 | 1.82 |
| 11-27 17:34 | +15 | NEAR | DOWN | 0.69 | 0.85 | 1.40 |
| 11-27 17:34 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.74 |
| 11-27 17:34 | +5 | NEAR | DOWN | 0.69 | 0.80 | 0.83 |
| 11-27 17:33 | +5 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-27 17:33 | +5 | ETH | DOWN | 0.62 | 0.71 | 0.58 |
| 11-27 17:33 | +5 | SOL | DOWN | 0.66 | 0.74 | 0.50 |
| 11-27 17:32 | +10 stop | BNB | DOWN | 0.65 | 0.49 | -1.94 |
| 11-27 17:32 | +10 | BNB | DOWN | 0.65 | 0.76 | 0.79 |
| 11-27 17:32 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.19 |
| 11-27 17:32 | +5 | BTC | DOWN | 0.66 | open |  |
| 11-27 17:32 | +10 stop | DOGE | DOWN | 0.69 | 0.54 | -1.83 |
| 11-27 17:32 | +20 | DOGE | DOWN | 0.69 | 0.93 | 2.16 |
| 11-27 17:32 | +15 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-27 17:32 | +10 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-27 17:32 | +5 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-27 17:32 | +10 stop | XRP | DOWN | 0.66 | 0.83 | 1.44 |
| 11-27 17:32 | +20 | XRP | DOWN | 0.66 | 0.87 | 1.86 |
| 11-27 17:32 | +15 | XRP | DOWN | 0.66 | 0.83 | 1.44 |
| 11-27 17:32 | +10 | XRP | DOWN | 0.66 | 0.83 | 1.44 |
| 11-27 17:32 | +5 | XRP | DOWN | 0.66 | 0.71 | 0.19 |
| 11-27 17:31 | +10 stop | ETH | DOWN | 0.66 | 0.49 | -2.04 |
| 11-27 17:31 | +20 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 11-27 17:31 | +15 | ETH | DOWN | 0.66 | 0.82 | 1.33 |
| 11-27 17:31 | +10 | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 11-27 17:31 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 11-27 17:31 | +10 stop | SOL | DOWN | 0.62 | 0.45 | -2.05 |
| 11-27 17:31 | +20 | SOL | DOWN | 0.62 | 0.82 | 1.72 |
| 11-27 17:31 | +15 | SOL | DOWN | 0.62 | 0.82 | 1.72 |
| 11-27 17:31 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
