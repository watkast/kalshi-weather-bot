# Range-Scalp Bot

*Updated Mon Oct 26 05:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34274 | 29921 | 4353 (43) | 0 | $-9497.55 | -4.4% |
| **+10¢** | 25652 | 20614 | 5038 (65) | 1 | $-8364.90 | -5.2% |
| **+15¢** | 21453 | 16029 | 5424 (89) | 1 | $-7489.85 | -5.6% |
| **+20¢** | 19017 | 13338 | 5679 (111) | 2 | $-6562.45 | -5.5% |
| **+10¢ (15¢ stop)** | 41986 | 41924 | 62 (33) | 0 | $-15995.87 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 05:01 | +10 stop | BNB | UP | 0.69 | 0.51 | -2.13 |
| 10-26 05:01 | +20 | BNB | UP | 0.69 | open |  |
| 10-26 05:01 | +15 | BNB | UP | 0.69 | open |  |
| 10-26 05:01 | +10 | BNB | UP | 0.69 | open |  |
| 10-26 05:01 | +5 | BNB | UP | 0.69 | 0.74 | 0.21 |
| 10-26 05:00 | +10 stop | HYPE | UP | 0.67 | 0.80 | 1.01 |
| 10-26 05:00 | +20 | HYPE | UP | 0.67 | open |  |
| 10-26 05:00 | +15 | HYPE | UP | 0.67 | 0.85 | 1.54 |
| 10-26 05:00 | +10 | HYPE | UP | 0.67 | 0.80 | 1.01 |
| 10-26 05:00 | +5 | HYPE | UP | 0.67 | 0.74 | 0.39 |
| 10-26 04:52 | +10 stop | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 10-26 04:51 | +10 stop | BTC | UP | 0.65 | 0.75 | 0.70 |
| 10-26 04:50 | +10 stop | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-26 04:50 | +10 stop | SOL | UP | 0.65 | 0.78 | 1.01 |
| 10-26 04:49 | +10 stop | XRP | UP | 0.54 | 0.78 | 2.09 |
| 10-26 04:49 | +5 | BNB | UP | 0.58 | 0.68 | 0.66 |
| 10-26 04:49 | +10 stop | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-26 04:49 | +15 | HYPE | UP | 0.66 | 0.81 | 1.23 |
| 10-26 04:49 | +10 | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-26 04:49 | +10 stop | NEAR | DOWN | 0.57 | 0.31 | -2.92 |
| 10-26 04:48 | +10 stop | ZEC | DOWN | 0.68 | 0.42 | -2.94 |
| 10-26 04:48 | +10 stop | ETH | UP | 0.55 | 0.67 | 0.86 |
| 10-26 04:48 | +10 stop | SOL | UP | 0.60 | 0.72 | 0.88 |
| 10-26 04:47 | +5 | HYPE | UP | 0.71 | 0.76 | 0.22 |
| 10-26 04:47 | +10 stop | BNB | UP | 0.54 | 0.68 | 1.06 |
| 10-26 04:47 | +20 | BNB | UP | 0.54 | 0.80 | 2.30 |
| 10-26 04:47 | +15 | BNB | UP | 0.54 | 0.80 | 2.30 |
| 10-26 04:47 | +10 | BNB | UP | 0.54 | 0.68 | 1.06 |
| 10-26 04:47 | +5 | BNB | UP | 0.54 | 0.61 | 0.35 |
| 10-26 04:47 | +10 stop | NEAR | DOWN | 0.62 | 0.47 | -1.85 |
| 10-26 04:47 | +20 | NEAR | DOWN | 0.62 | yes | -6.37 |
| 10-26 04:47 | +15 | NEAR | DOWN | 0.62 | yes | -6.37 |
| 10-26 04:47 | +10 | NEAR | DOWN | 0.62 | yes | -6.37 |
| 10-26 04:47 | +5 | NEAR | DOWN | 0.62 | yes | -6.37 |
| 10-26 04:46 | +10 stop | BTC | DOWN | 0.59 | 0.44 | -1.85 |
| 10-26 04:46 | +20 | BTC | DOWN | 0.59 | yes | -6.07 |
| 10-26 04:46 | +15 | BTC | DOWN | 0.59 | yes | -6.07 |
| 10-26 04:46 | +10 | BTC | DOWN | 0.59 | yes | -6.07 |
| 10-26 04:46 | +5 | BTC | DOWN | 0.59 | yes | -6.07 |
| 10-26 04:46 | +10 stop | DOGE | DOWN | 0.59 | 0.41 | -2.14 |
