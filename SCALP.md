# Range-Scalp Bot

*Updated Mon Oct 26 21:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35457 | 30944 | 4513 (43) | 7 | $-9931.56 | -4.4% |
| **+10¢** | 26516 | 21294 | 5222 (65) | 7 | $-8778.31 | -5.3% |
| **+15¢** | 22189 | 16571 | 5618 (89) | 7 | $-7864.00 | -5.6% |
| **+20¢** | 19675 | 13787 | 5888 (112) | 7 | $-6925.93 | -5.6% |
| **+10¢ (15¢ stop)** | 43482 | 43420 | 62 (33) | 0 | $-16559.82 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 21:34 | +10 stop | ZEC | UP | 0.70 | 0.81 | 0.85 |
| 10-26 21:34 | +10 stop | ETH | UP | 0.68 | 0.78 | 0.71 |
| 10-26 21:34 | +10 stop | BTC | UP | 0.61 | 0.71 | 0.68 |
| 10-26 21:34 | +20 | BTC | UP | 0.61 | 0.86 | 2.24 |
| 10-26 21:34 | +15 | BTC | UP | 0.61 | 0.76 | 1.20 |
| 10-26 21:34 | +10 | BTC | UP | 0.61 | 0.71 | 0.68 |
| 10-26 21:34 | +5 | BTC | UP | 0.61 | 0.71 | 0.68 |
| 10-26 21:33 | +10 stop | XRP | UP | 0.66 | 0.83 | 1.44 |
| 10-26 21:33 | +15 | XRP | UP | 0.66 | 0.83 | 1.44 |
| 10-26 21:33 | +10 | XRP | UP | 0.67 | 0.83 | 1.34 |
| 10-26 21:33 | +5 | XRP | UP | 0.66 | 0.71 | 0.19 |
| 10-26 21:33 | +10 stop | DOGE | UP | 0.61 | 0.76 | 1.20 |
| 10-26 21:32 | +10 stop | BNB | UP | 0.61 | 0.72 | 0.78 |
| 10-26 21:32 | +5 | HYPE | DOWN | 0.57 | open |  |
| 10-26 21:32 | +10 stop | NEAR | DOWN | 0.56 | 0.36 | -2.35 |
| 10-26 21:32 | +20 | NEAR | DOWN | 0.56 | open |  |
| 10-26 21:32 | +15 | NEAR | DOWN | 0.56 | open |  |
| 10-26 21:32 | +10 | NEAR | DOWN | 0.56 | open |  |
| 10-26 21:32 | +5 | NEAR | DOWN | 0.56 | open |  |
| 10-26 21:32 | +10 stop | XRP | UP | 0.57 | 0.73 | 1.28 |
| 10-26 21:32 | +20 | XRP | UP | 0.57 | 0.83 | 2.32 |
| 10-26 21:32 | +15 | XRP | UP | 0.57 | 0.73 | 1.28 |
| 10-26 21:32 | +10 | XRP | UP | 0.57 | 0.73 | 1.28 |
| 10-26 21:32 | +5 | XRP | UP | 0.56 | 0.73 | 1.38 |
| 10-26 21:31 | +10 stop | ETH | DOWN | 0.58 | 0.40 | -2.15 |
| 10-26 21:31 | +20 | ETH | DOWN | 0.58 | open |  |
| 10-26 21:31 | +15 | ETH | DOWN | 0.58 | open |  |
| 10-26 21:31 | +10 | ETH | DOWN | 0.58 | open |  |
| 10-26 21:31 | +5 | ETH | DOWN | 0.58 | open |  |
| 10-26 21:31 | +10 stop | HYPE | DOWN | 0.57 | 0.41 | -1.95 |
| 10-26 21:31 | +20 | HYPE | DOWN | 0.57 | open |  |
| 10-26 21:31 | +15 | HYPE | DOWN | 0.57 | open |  |
| 10-26 21:31 | +10 | HYPE | DOWN | 0.57 | open |  |
| 10-26 21:31 | +5 | HYPE | DOWN | 0.57 | 0.63 | 0.25 |
| 10-26 21:31 | +10 stop | BNB | DOWN | 0.57 | 0.42 | -1.86 |
| 10-26 21:31 | +20 | BNB | DOWN | 0.57 | open |  |
| 10-26 21:31 | +15 | BNB | DOWN | 0.57 | open |  |
| 10-26 21:31 | +10 | BNB | DOWN | 0.57 | open |  |
| 10-26 21:31 | +5 | BNB | DOWN | 0.57 | open |  |
| 10-26 21:31 | +10 stop | SOL | DOWN | 0.58 | 0.29 | -3.23 |
