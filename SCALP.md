# Range-Scalp Bot

*Updated Fri Nov 20 03:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65760 | 57399 | 8361 (124) | 5 | $-17645.34 | -4.3% |
| **+10¢** | 49111 | 39335 | 9776 (165) | 7 | $-16412.88 | -5.3% |
| **+15¢** | 41186 | 30642 | 10544 (211) | 8 | $-14774.71 | -5.7% |
| **+20¢** | 36664 | 25588 | 11076 (267) | 8 | $-13082.61 | -5.7% |
| **+10¢ (15¢ stop)** | 80059 | 79895 | 164 (98) | 1 | $-29485.25 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 03:05 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 11-20 03:04 | +10 stop | SOL | DOWN | 0.59 | 0.71 | 0.88 |
| 11-20 03:04 | +10 stop | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 11-20 03:04 | +10 stop | HYPE | DOWN | 0.66 | 0.80 | 1.12 |
| 11-20 03:04 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 11-20 03:04 | +10 | HYPE | DOWN | 0.68 | 0.80 | 0.92 |
| 11-20 03:04 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.30 |
| 11-20 03:03 | +10 stop | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-20 03:03 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.19 |
| 11-20 03:03 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-20 03:03 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-20 03:03 | +10 stop | BTC | UP | 0.57 | 0.39 | -2.15 |
| 11-20 03:03 | +10 | BTC | UP | 0.57 | open |  |
| 11-20 03:03 | +5 | BTC | UP | 0.57 | open |  |
| 11-20 03:03 | +10 stop | NEAR | DOWN | 0.68 | 0.80 | 0.93 |
| 11-20 03:03 | +20 | NEAR | DOWN | 0.68 | 0.89 | 1.88 |
| 11-20 03:03 | +15 | NEAR | DOWN | 0.67 | 0.85 | 1.55 |
| 11-20 03:03 | +10 | NEAR | DOWN | 0.66 | 0.80 | 1.12 |
| 11-20 03:03 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.30 |
| 11-20 03:03 | +10 stop | HYPE | UP | 0.51 | 0.34 | -2.08 |
| 11-20 03:03 | +10 | HYPE | UP | 0.50 | 0.61 | 0.75 |
| 11-20 03:03 | +5 | HYPE | UP | 0.51 | 0.61 | 0.65 |
| 11-20 03:02 | +10 stop | DOGE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-20 03:02 | +5 | BTC | UP | 0.54 | 0.73 | 1.58 |
| 11-20 03:01 | +10 stop | BTC | UP | 0.61 | 0.73 | 0.89 |
| 11-20 03:01 | +20 | BTC | UP | 0.61 | open |  |
| 11-20 03:01 | +15 | BTC | UP | 0.61 | open |  |
| 11-20 03:01 | +10 | BTC | UP | 0.61 | 0.73 | 0.89 |
| 11-20 03:01 | +5 | BTC | UP | 0.61 | 0.66 | 0.17 |
| 11-20 03:01 | +10 stop | HYPE | UP | 0.54 | 0.66 | 0.86 |
| 11-20 03:01 | +20 | HYPE | UP | 0.54 | open |  |
| 11-20 03:01 | +15 | HYPE | UP | 0.53 | open |  |
| 11-20 03:01 | +10 | HYPE | UP | 0.54 | 0.66 | 0.86 |
| 11-20 03:01 | +5 | HYPE | UP | 0.55 | 0.66 | 0.76 |
| 11-20 03:01 | +10 stop | BNB | UP | 0.52 | 0.34 | -2.14 |
| 11-20 03:01 | +20 | BNB | UP | 0.52 | open |  |
| 11-20 03:01 | +15 | BNB | UP | 0.51 | open |  |
| 11-20 03:01 | +10 | BNB | UP | 0.51 | open |  |
| 11-20 03:01 | +5 | BNB | UP | 0.51 | 0.60 | 0.55 |
| 11-20 03:01 | +10 stop | ZEC | UP | 0.52 | 0.31 | -2.43 |
