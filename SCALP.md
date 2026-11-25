# Range-Scalp Bot

*Updated Wed Nov 25 05:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71463 | 62378 | 9085 (156) | 1 | $-19028.10 | -4.2% |
| **+10¢** | 53300 | 42688 | 10612 (202) | 2 | $-17638.61 | -5.3% |
| **+15¢** | 44641 | 33217 | 11424 (259) | 2 | $-15664.95 | -5.6% |
| **+20¢** | 39743 | 27711 | 12032 (325) | 3 | $-14081.91 | -5.6% |
| **+10¢ (15¢ stop)** | 87006 | 86803 | 203 (123) | 0 | $-31995.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 05:11 | +10 stop | SOL | DOWN | 0.46 | 0.71 | 2.19 |
| 11-25 05:11 | +20 | SOL | DOWN | 0.46 | 0.71 | 2.19 |
| 11-25 05:11 | +15 | SOL | DOWN | 0.46 | 0.71 | 2.19 |
| 11-25 05:11 | +10 | SOL | DOWN | 0.46 | 0.71 | 2.20 |
| 11-25 05:11 | +5 | SOL | DOWN | 0.44 | 0.53 | 0.54 |
| 11-25 05:11 | +10 stop | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 11-25 05:11 | +10 stop | HYPE | DOWN | 0.55 | 0.72 | 1.41 |
| 11-25 05:11 | +15 | HYPE | DOWN | 0.55 | 0.72 | 1.41 |
| 11-25 05:11 | +10 | HYPE | DOWN | 0.55 | 0.72 | 1.41 |
| 11-25 05:11 | +5 | HYPE | DOWN | 0.55 | 0.62 | 0.39 |
| 11-25 05:11 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 11-25 05:11 | +20 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 11-25 05:11 | +15 | XRP | DOWN | 0.61 | 0.78 | 1.40 |
| 11-25 05:11 | +10 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 11-25 05:11 | +5 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 11-25 05:10 | +5 | ETH | UP | 0.66 | open |  |
| 11-25 05:09 | +10 stop | ETH | UP | 0.63 | 0.38 | -2.84 |
| 11-25 05:08 | +10 stop | BTC | UP | 0.61 | 0.28 | -3.62 |
| 11-25 05:08 | +20 | BTC | UP | 0.61 | open |  |
| 11-25 05:08 | +15 | BTC | UP | 0.61 | open |  |
| 11-25 05:08 | +10 | BTC | UP | 0.61 | open |  |
| 11-25 05:07 | +10 stop | HYPE | UP | 0.58 | 0.73 | 1.18 |
| 11-25 05:07 | +10 stop | ETH | UP | 0.51 | 0.64 | 0.95 |
| 11-25 05:07 | +10 stop | SOL | UP | 0.60 | 0.72 | 0.88 |
| 11-25 05:07 | +5 | SOL | UP | 0.61 | 0.68 | 0.37 |
| 11-25 05:07 | +5 | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 11-25 05:06 | +10 stop | DOGE | UP | 0.60 | 0.70 | 0.68 |
| 11-25 05:06 | +10 stop | SOL | DOWN | 0.57 | 0.37 | -2.35 |
| 11-25 05:05 | +10 stop | HYPE | DOWN | 0.66 | 0.38 | -3.13 |
| 11-25 05:05 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-25 05:05 | +10 stop | XRP | UP | 0.64 | 0.74 | 0.70 |
| 11-25 05:05 | +10 stop | BTC | UP | 0.55 | 0.76 | 1.79 |
| 11-25 05:05 | +10 stop | ETH | DOWN | 0.56 | 0.37 | -2.25 |
| 11-25 05:05 | +5 | BNB | UP | 0.70 | 0.75 | 0.22 |
| 11-25 05:05 | +10 stop | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 11-25 05:05 | +10 | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 11-25 05:05 | +5 | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 11-25 05:05 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-25 05:04 | +10 stop | XRP | UP | 0.47 | 0.57 | 0.64 |
| 11-25 05:04 | +10 stop | HYPE | DOWN | 0.56 | 0.70 | 1.07 |
