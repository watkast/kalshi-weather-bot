# Range-Scalp Bot

*Updated Sun Oct 18 12:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22545 | 19627 | 2918 (29) | 2 | $-6573.39 | -4.6% |
| **+10¢** | 16963 | 13591 | 3372 (43) | 2 | $-5850.97 | -5.5% |
| **+15¢** | 14203 | 10563 | 3640 (63) | 2 | $-5360.32 | -6.0% |
| **+20¢** | 12572 | 8761 | 3811 (81) | 2 | $-4779.45 | -6.1% |
| **+10¢ (15¢ stop)** | 27716 | 27666 | 50 (29) | 0 | $-10572.73 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 12:10 | +10 stop | NEAR | UP | 0.71 | 0.89 | 1.58 |
| 10-18 12:10 | +20 | NEAR | UP | 0.71 | 0.94 | 2.05 |
| 10-18 12:10 | +15 | NEAR | UP | 0.71 | 0.89 | 1.58 |
| 10-18 12:10 | +10 | NEAR | UP | 0.71 | 0.89 | 1.58 |
| 10-18 12:10 | +5 | NEAR | UP | 0.71 | 0.89 | 1.58 |
| 10-18 12:04 | +10 | NEAR | UP | 0.67 | 0.80 | 1.02 |
| 10-18 12:04 | +5 | NEAR | UP | 0.67 | 0.74 | 0.40 |
| 10-18 12:03 | +10 stop | BTC | UP | 0.71 | 0.87 | 1.37 |
| 10-18 12:02 | +10 stop | BTC | UP | 0.53 | 0.66 | 0.96 |
| 10-18 12:02 | +10 stop | NEAR | UP | 0.62 | 0.74 | 0.92 |
| 10-18 12:02 | +20 | NEAR | UP | 0.61 | 0.81 | 1.72 |
| 10-18 12:02 | +15 | NEAR | UP | 0.61 | 0.80 | 1.61 |
| 10-18 12:02 | +10 | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-18 12:02 | +5 | NEAR | UP | 0.61 | 0.70 | 0.58 |
| 10-18 12:01 | +10 stop | HYPE | UP | 0.71 | 0.88 | 1.47 |
| 10-18 12:00 | +10 stop | XRP | UP | 0.66 | 0.84 | 1.54 |
| 10-18 12:00 | +20 | XRP | UP | 0.66 | 0.86 | 1.75 |
| 10-18 12:00 | +15 | XRP | UP | 0.66 | 0.84 | 1.54 |
| 10-18 12:00 | +10 | XRP | UP | 0.66 | 0.84 | 1.54 |
| 10-18 12:00 | +5 | XRP | UP | 0.66 | 0.74 | 0.50 |
| 10-18 12:00 | +10 stop | BTC | DOWN | 0.65 | 0.45 | -2.34 |
| 10-18 12:00 | +20 | BTC | DOWN | 0.65 | open |  |
| 10-18 12:00 | +15 | BTC | DOWN | 0.65 | open |  |
| 10-18 12:00 | +10 | BTC | DOWN | 0.65 | open |  |
| 10-18 12:00 | +5 | BTC | DOWN | 0.65 | open |  |
| 10-18 12:00 | +10 stop | HYPE | DOWN | 0.57 | 0.41 | -1.95 |
| 10-18 12:00 | +20 | HYPE | DOWN | 0.57 | open |  |
| 10-18 12:00 | +15 | HYPE | DOWN | 0.57 | open |  |
| 10-18 12:00 | +10 | HYPE | DOWN | 0.57 | open |  |
| 10-18 12:00 | +5 | HYPE | DOWN | 0.57 | open |  |
| 10-18 11:58 | +10 stop | BTC | UP | 0.65 | 0.91 | 2.39 |
| 10-18 11:57 | +10 stop | SOL | DOWN | 0.66 | 0.47 | -2.24 |
| 10-18 11:57 | +15 | SOL | DOWN | 0.66 | yes | -6.76 |
| 10-18 11:57 | +10 | SOL | DOWN | 0.66 | yes | -6.76 |
| 10-18 11:57 | +5 | SOL | DOWN | 0.66 | yes | -6.76 |
| 10-18 11:56 | +10 stop | BTC | DOWN | 0.60 | 0.45 | -1.85 |
| 10-18 11:55 | +10 stop | BTC | DOWN | 0.51 | 0.62 | 0.75 |
| 10-18 11:54 | +10 stop | BNB | UP | 0.69 | 0.91 | 1.98 |
| 10-18 11:53 | +5 | ETH | UP | 0.64 | 0.71 | 0.38 |
| 10-18 11:52 | +5 | ETH | UP | 0.59 | 0.66 | 0.37 |
