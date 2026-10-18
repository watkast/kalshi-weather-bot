# Range-Scalp Bot

*Updated Sun Oct 18 04:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22018 | 19175 | 2843 (29) | 0 | $-6355.92 | -4.6% |
| **+10¢** | 16571 | 13287 | 3284 (41) | 1 | $-5648.50 | -5.4% |
| **+15¢** | 13878 | 10337 | 3541 (61) | 1 | $-5117.06 | -5.9% |
| **+20¢** | 12281 | 8571 | 3710 (80) | 1 | $-4561.93 | -5.9% |
| **+10¢ (15¢ stop)** | 27088 | 27038 | 50 (29) | 0 | $-10346.90 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 04:02 | +10 stop | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-18 04:02 | +10 | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-18 04:02 | +5 | BTC | DOWN | 0.70 | 0.78 | 0.52 |
| 10-18 04:02 | +10 stop | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-18 04:02 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.30 |
| 10-18 04:01 | +10 stop | NEAR | DOWN | 0.59 | 0.72 | 0.98 |
| 10-18 04:01 | +20 | NEAR | DOWN | 0.59 | 0.79 | 1.71 |
| 10-18 04:01 | +15 | NEAR | DOWN | 0.59 | 0.76 | 1.40 |
| 10-18 04:01 | +10 | NEAR | DOWN | 0.59 | 0.72 | 0.98 |
| 10-18 04:01 | +5 | NEAR | DOWN | 0.59 | 0.66 | 0.37 |
| 10-18 04:01 | +10 stop | ZEC | DOWN | 0.69 | 0.85 | 1.40 |
| 10-18 04:01 | +20 | ZEC | DOWN | 0.68 | 0.90 | 2.00 |
| 10-18 04:01 | +15 | ZEC | DOWN | 0.69 | 0.85 | 1.40 |
| 10-18 04:01 | +10 | ZEC | DOWN | 0.69 | 0.85 | 1.40 |
| 10-18 04:01 | +5 | ZEC | DOWN | 0.67 | 0.76 | 0.62 |
| 10-18 04:01 | +10 stop | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 10-18 04:01 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.88 |
| 10-18 04:01 | +15 | XRP | DOWN | 0.70 | 0.88 | 1.57 |
| 10-18 04:01 | +10 | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 10-18 04:01 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 10-18 04:00 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-18 04:00 | +20 | BTC | DOWN | 0.64 | 0.84 | 1.73 |
| 10-18 04:00 | +15 | BTC | DOWN | 0.64 | 0.81 | 1.42 |
| 10-18 04:00 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-18 04:00 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-18 04:00 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-18 04:00 | +20 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 10-18 04:00 | +15 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 10-18 04:00 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-18 04:00 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 10-18 04:00 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 10-18 04:00 | +20 | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 10-18 04:00 | +15 | BNB | DOWN | 0.61 | 0.78 | 1.40 |
| 10-18 04:00 | +10 | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 10-18 04:00 | +5 | BNB | DOWN | 0.61 | 0.69 | 0.48 |
| 10-18 04:00 | +10 stop | HYPE | UP | 0.54 | 0.37 | -2.09 |
| 10-18 04:00 | +20 | HYPE | UP | 0.53 | open |  |
| 10-18 04:00 | +15 | HYPE | UP | 0.53 | open |  |
| 10-18 04:00 | +10 | HYPE | UP | 0.53 | open |  |
| 10-18 04:00 | +5 | HYPE | UP | 0.53 | 0.63 | 0.61 |
