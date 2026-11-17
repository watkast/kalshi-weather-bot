# Range-Scalp Bot

*Updated Tue Nov 17 05:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62608 | 54615 | 7993 (117) | 0 | $-17004.02 | -4.3% |
| **+10¢** | 46756 | 37404 | 9352 (159) | 0 | $-15879.07 | -5.4% |
| **+15¢** | 39188 | 29102 | 10086 (201) | 1 | $-14426.14 | -5.9% |
| **+20¢** | 34931 | 24355 | 10576 (256) | 1 | $-12590.30 | -5.7% |
| **+10¢ (15¢ stop)** | 76194 | 76038 | 156 (92) | 0 | $-28085.80 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 05:04 | +5 | ZEC | DOWN | 0.70 | 0.79 | 0.63 |
| 11-17 05:03 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-17 05:01 | +10 stop | ZEC | DOWN | 0.65 | 0.79 | 1.12 |
| 11-17 05:01 | +20 | ZEC | DOWN | 0.65 | open |  |
| 11-17 05:01 | +15 | ZEC | DOWN | 0.66 | open |  |
| 11-17 05:01 | +10 | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-17 05:01 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.19 |
| 11-17 05:00 | +10 stop | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 11-17 05:00 | +20 | HYPE | DOWN | 0.60 | 0.81 | 1.82 |
| 11-17 05:00 | +15 | HYPE | DOWN | 0.60 | 0.81 | 1.82 |
| 11-17 05:00 | +10 | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 11-17 05:00 | +5 | HYPE | DOWN | 0.60 | 0.67 | 0.37 |
| 11-17 04:56 | +5 | DOGE | UP | 0.58 | 0.65 | 0.36 |
| 11-17 04:56 | +5 | BTC | DOWN | 0.60 | yes | -6.17 |
| 11-17 04:55 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 11-17 04:55 | +5 | BTC | DOWN | 0.58 | 0.65 | 0.36 |
| 11-17 04:55 | +10 stop | BNB | DOWN | 0.61 | 0.27 | -3.71 |
| 11-17 04:54 | +10 stop | DOGE | DOWN | 0.65 | 0.45 | -2.30 |
| 11-17 04:54 | +10 stop | XRP | DOWN | 0.68 | 0.50 | -2.14 |
| 11-17 04:54 | +20 | XRP | DOWN | 0.69 | yes | -7.05 |
| 11-17 04:54 | +15 | XRP | DOWN | 0.67 | yes | -6.86 |
| 11-17 04:54 | +10 | XRP | DOWN | 0.67 | yes | -6.86 |
| 11-17 04:53 | +10 stop | HYPE | UP | 0.62 | 0.75 | 0.99 |
| 11-17 04:53 | +10 stop | BTC | DOWN | 0.66 | 0.42 | -2.74 |
| 11-17 04:53 | +20 | BTC | DOWN | 0.66 | yes | -6.76 |
| 11-17 04:53 | +15 | BTC | DOWN | 0.66 | yes | -6.76 |
| 11-17 04:53 | +10 | BTC | DOWN | 0.66 | yes | -6.76 |
| 11-17 04:53 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-17 04:53 | +10 stop | NEAR | UP | 0.61 | 0.74 | 0.99 |
| 11-17 04:51 | +10 stop | ETH | DOWN | 0.56 | 0.33 | -2.64 |
| 11-17 04:51 | +10 stop | ZEC | UP | 0.64 | 0.76 | 0.90 |
| 11-17 04:51 | +20 | ZEC | UP | 0.64 | 0.85 | 1.84 |
| 11-17 04:51 | +5 | ZEC | UP | 0.64 | 0.72 | 0.48 |
| 11-17 04:51 | +10 stop | NEAR | DOWN | 0.60 | 0.43 | -2.03 |
| 11-17 04:50 | +10 stop | BNB | DOWN | 0.67 | 0.48 | -2.24 |
| 11-17 04:50 | +10 stop | HYPE | DOWN | 0.69 | 0.40 | -3.22 |
| 11-17 04:50 | +10 | HYPE | DOWN | 0.69 | yes | -7.05 |
| 11-17 04:50 | +15 | ZEC | UP | 0.70 | 0.85 | 1.26 |
| 11-17 04:50 | +10 | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 11-17 04:50 | +5 | ZEC | UP | 0.70 | 0.77 | 0.42 |
