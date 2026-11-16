# Range-Scalp Bot

*Updated Mon Nov 16 09:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61797 | 53915 | 7882 (115) | 0 | $-16706.70 | -4.3% |
| **+10¢** | 46166 | 36935 | 9231 (157) | 0 | $-15614.32 | -5.4% |
| **+15¢** | 38688 | 28731 | 9957 (196) | 1 | $-14239.85 | -5.9% |
| **+20¢** | 34491 | 24049 | 10442 (249) | 2 | $-12446.25 | -5.8% |
| **+10¢ (15¢ stop)** | 75214 | 75060 | 154 (90) | 0 | $-27706.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 09:01 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-16 09:01 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-16 09:01 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-16 09:01 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-16 09:01 | +5 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-16 09:01 | +10 stop | SOL | DOWN | 0.66 | 0.84 | 1.54 |
| 11-16 09:01 | +20 | SOL | DOWN | 0.66 | open |  |
| 11-16 09:01 | +15 | SOL | DOWN | 0.66 | 0.84 | 1.54 |
| 11-16 09:01 | +10 | SOL | DOWN | 0.65 | 0.84 | 1.64 |
| 11-16 09:01 | +5 | SOL | DOWN | 0.65 | 0.72 | 0.39 |
| 11-16 08:57 | +10 stop | HYPE | DOWN | 0.61 | 0.41 | -2.34 |
| 11-16 08:57 | +20 | HYPE | DOWN | 0.61 | yes | -6.27 |
| 11-16 08:57 | +15 | HYPE | DOWN | 0.63 | yes | -6.47 |
| 11-16 08:57 | +10 | HYPE | DOWN | 0.62 | yes | -6.37 |
| 11-16 08:57 | +5 | HYPE | DOWN | 0.62 | yes | -6.37 |
| 11-16 08:53 | +10 stop | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 11-16 08:52 | +10 stop | DOGE | DOWN | 0.62 | 0.80 | 1.51 |
| 11-16 08:52 | +10 stop | NEAR | UP | 0.66 | 0.37 | -3.23 |
| 11-16 08:51 | +10 stop | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 11-16 08:51 | +10 stop | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 11-16 08:51 | +10 stop | ETH | UP | 0.44 | 0.69 | 2.17 |
| 11-16 08:51 | +20 | ETH | UP | 0.44 | 0.69 | 2.17 |
| 11-16 08:51 | +15 | ETH | UP | 0.44 | 0.69 | 2.17 |
| 11-16 08:51 | +10 | ETH | UP | 0.46 | 0.69 | 1.97 |
| 11-16 08:51 | +5 | ETH | UP | 0.46 | 0.69 | 1.97 |
| 11-16 08:51 | +10 stop | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-16 08:51 | +10 stop | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-16 08:51 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-16 08:50 | +10 stop | DOGE | UP | 0.70 | 0.53 | -2.03 |
| 11-16 08:50 | +5 | DOGE | UP | 0.70 | no | -7.15 |
| 11-16 08:49 | +5 | SOL | UP | 0.69 | no | -7.05 |
| 11-16 08:49 | +10 stop | XRP | DOWN | 0.65 | 0.84 | 1.64 |
| 11-16 08:49 | +20 | XRP | DOWN | 0.65 | 0.87 | 1.96 |
| 11-16 08:49 | +15 | XRP | DOWN | 0.65 | 0.84 | 1.64 |
| 11-16 08:49 | +10 | XRP | DOWN | 0.65 | 0.84 | 1.64 |
| 11-16 08:49 | +5 | XRP | DOWN | 0.65 | 0.74 | 0.60 |
| 11-16 08:49 | +10 stop | BNB | UP | 0.60 | 0.34 | -2.93 |
| 11-16 08:49 | +20 | BNB | UP | 0.61 | no | -6.27 |
| 11-16 08:49 | +15 | BNB | UP | 0.61 | no | -6.27 |
| 11-16 08:49 | +10 | BNB | UP | 0.61 | no | -6.27 |
