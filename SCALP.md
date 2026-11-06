# Range-Scalp Bot

*Updated Fri Nov 06 14:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49603 | 43235 | 6368 (76) | 3 | $-13961.12 | -4.5% |
| **+10¢** | 37023 | 29618 | 7405 (101) | 5 | $-12836.07 | -5.5% |
| **+15¢** | 31009 | 23030 | 7979 (130) | 5 | $-11744.74 | -6.0% |
| **+20¢** | 27565 | 19202 | 8363 (171) | 5 | $-10369.90 | -6.0% |
| **+10¢ (15¢ stop)** | 60438 | 60341 | 97 (57) | 0 | $-22333.07 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 14:39 | +10 stop | ETH | UP | 0.67 | 0.82 | 1.23 |
| 11-06 14:37 | +5 | BTC | DOWN | 0.33 | 0.64 | 2.77 |
| 11-06 14:37 | +10 stop | BTC | DOWN | 0.66 | 0.35 | -3.42 |
| 11-06 14:37 | +20 | BTC | DOWN | 0.65 | open |  |
| 11-06 14:37 | +15 | BTC | DOWN | 0.63 | open |  |
| 11-06 14:37 | +10 | BTC | DOWN | 0.62 | open |  |
| 11-06 14:37 | +5 | BTC | DOWN | 0.62 | 0.69 | 0.38 |
| 11-06 14:37 | +5 | SOL | DOWN | 0.58 | open |  |
| 11-06 14:36 | +10 stop | HYPE | DOWN | 0.52 | 0.63 | 0.75 |
| 11-06 14:36 | +20 | HYPE | DOWN | 0.57 | open |  |
| 11-06 14:36 | +15 | HYPE | DOWN | 0.57 | open |  |
| 11-06 14:36 | +10 | HYPE | DOWN | 0.56 | open |  |
| 11-06 14:36 | +5 | HYPE | DOWN | 0.57 | 0.63 | 0.25 |
| 11-06 14:36 | +10 stop | DOGE | UP | 0.65 | 0.86 | 1.85 |
| 11-06 14:36 | +5 | DOGE | UP | 0.65 | 0.74 | 0.60 |
| 11-06 14:36 | +10 stop | XRP | UP | 0.63 | 0.76 | 1.00 |
| 11-06 14:36 | +10 | XRP | UP | 0.62 | 0.76 | 1.10 |
| 11-06 14:36 | +5 | XRP | UP | 0.62 | 0.70 | 0.48 |
| 11-06 14:36 | +10 stop | SOL | DOWN | 0.63 | 0.33 | -3.33 |
| 11-06 14:36 | +10 | SOL | DOWN | 0.62 | open |  |
| 11-06 14:36 | +5 | SOL | DOWN | 0.62 | 0.68 | 0.27 |
| 11-06 14:36 | +10 stop | ETH | DOWN | 0.68 | 0.38 | -3.33 |
| 11-06 14:36 | +15 | ETH | DOWN | 0.68 | open |  |
| 11-06 14:36 | +10 | ETH | DOWN | 0.68 | open |  |
| 11-06 14:36 | +5 | ETH | DOWN | 0.68 | open |  |
| 11-06 14:36 | +10 stop | BNB | DOWN | 0.68 | 0.51 | -2.05 |
| 11-06 14:36 | +15 | BNB | DOWN | 0.68 | open |  |
| 11-06 14:36 | +10 | BNB | DOWN | 0.68 | open |  |
| 11-06 14:36 | +5 | BNB | DOWN | 0.68 | open |  |
| 11-06 14:36 | +10 stop | DOGE | DOWN | 0.37 | 0.56 | 1.55 |
| 11-06 14:36 | +5 | DOGE | DOWN | 0.38 | 0.56 | 1.45 |
| 11-06 14:35 | +10 stop | XRP | DOWN | 0.50 | 0.60 | 0.65 |
| 11-06 14:35 | +20 | XRP | DOWN | 0.50 | open |  |
| 11-06 14:35 | +15 | XRP | DOWN | 0.49 | open |  |
| 11-06 14:35 | +10 | XRP | DOWN | 0.49 | 0.60 | 0.75 |
| 11-06 14:35 | +5 | XRP | DOWN | 0.50 | 0.60 | 0.65 |
| 11-06 14:34 | +5 | NEAR | UP | 0.67 | 0.74 | 0.40 |
| 11-06 14:34 | +10 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-06 14:33 | +10 stop | ZEC | UP | 0.63 | 0.91 | 2.53 |
| 11-06 14:33 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
