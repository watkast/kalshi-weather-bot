# Range-Scalp Bot

*Updated Fri Nov 27 15:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73645 | 64265 | 9380 (171) | 8 | $-19612.78 | -4.2% |
| **+10¢** | 54885 | 43932 | 10953 (216) | 8 | $-18239.37 | -5.3% |
| **+15¢** | 45959 | 34161 | 11798 (274) | 8 | $-16345.12 | -5.7% |
| **+20¢** | 40900 | 28477 | 12423 (340) | 9 | $-14755.54 | -5.8% |
| **+10¢ (15¢ stop)** | 89691 | 89472 | 219 (135) | 4 | $-33147.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 15:26 | +10 stop | DOGE | DOWN | 0.63 | open |  |
| 11-27 15:26 | +10 stop | ZEC | UP | 0.67 | open |  |
| 11-27 15:26 | +5 | ZEC | UP | 0.68 | open |  |
| 11-27 15:26 | +10 stop | DOGE | UP | 0.40 | 0.54 | 1.05 |
| 11-27 15:25 | +10 stop | HYPE | UP | 0.60 | open |  |
| 11-27 15:25 | +10 stop | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 11-27 15:25 | +20 | SOL | UP | 0.62 | open |  |
| 11-27 15:25 | +15 | SOL | UP | 0.63 | open |  |
| 11-27 15:25 | +5 | SOL | UP | 0.63 | open |  |
| 11-27 15:25 | +10 stop | XRP | UP | 0.51 | 0.25 | -2.92 |
| 11-27 15:24 | +5 | XRP | UP | 0.69 | open |  |
| 11-27 15:24 | +10 | SOL | UP | 0.66 | open |  |
| 11-27 15:24 | +10 stop | SOL | UP | 0.66 | 0.48 | -2.14 |
| 11-27 15:24 | +5 | SOL | UP | 0.66 | 0.75 | 0.60 |
| 11-27 15:24 | +10 stop | BNB | UP | 0.70 | open |  |
| 11-27 15:24 | +10 stop | BTC | UP | 0.70 | 0.82 | 0.94 |
| 11-27 15:24 | +10 stop | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 11-27 15:24 | +10 stop | XRP | DOWN | 0.52 | 0.33 | -2.24 |
| 11-27 15:24 | +15 | XRP | DOWN | 0.50 | 0.74 | 2.08 |
| 11-27 15:24 | +10 | XRP | DOWN | 0.50 | 0.74 | 2.08 |
| 11-27 15:24 | +5 | XRP | DOWN | 0.50 | 0.58 | 0.44 |
| 11-27 15:24 | +10 stop | ETH | UP | 0.67 | 0.82 | 1.23 |
| 11-27 15:23 | +10 stop | SOL | DOWN | 0.53 | 0.63 | 0.65 |
| 11-27 15:23 | +5 | SOL | DOWN | 0.54 | 0.63 | 0.55 |
| 11-27 15:23 | +10 stop | HYPE | DOWN | 0.58 | 0.41 | -2.05 |
| 11-27 15:23 | +20 | HYPE | DOWN | 0.58 | open |  |
| 11-27 15:23 | +15 | HYPE | DOWN | 0.58 | open |  |
| 11-27 15:23 | +10 | HYPE | DOWN | 0.56 | open |  |
| 11-27 15:23 | +5 | HYPE | DOWN | 0.56 | open |  |
| 11-27 15:23 | +10 stop | BTC | DOWN | 0.63 | 0.43 | -2.35 |
| 11-27 15:23 | +20 | BTC | DOWN | 0.63 | open |  |
| 11-27 15:23 | +15 | BTC | DOWN | 0.64 | open |  |
| 11-27 15:23 | +10 | BTC | DOWN | 0.64 | open |  |
| 11-27 15:23 | +5 | BTC | DOWN | 0.64 | open |  |
| 11-27 15:23 | +10 stop | NEAR | DOWN | 0.67 | 0.44 | -2.64 |
| 11-27 15:23 | +20 | NEAR | DOWN | 0.67 | open |  |
| 11-27 15:23 | +15 | NEAR | DOWN | 0.67 | open |  |
| 11-27 15:23 | +10 | NEAR | DOWN | 0.67 | open |  |
| 11-27 15:23 | +5 | NEAR | DOWN | 0.68 | 0.76 | 0.51 |
| 11-27 15:23 | +10 stop | BNB | DOWN | 0.70 | 0.49 | -2.43 |
