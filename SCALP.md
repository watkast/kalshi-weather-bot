# Range-Scalp Bot

*Updated Sat Nov 07 09:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50798 | 44286 | 6512 (76) | 1 | $-14225.02 | -4.4% |
| **+10¢** | 37921 | 30334 | 7587 (102) | 2 | $-13180.32 | -5.5% |
| **+15¢** | 31745 | 23572 | 8173 (131) | 3 | $-12077.97 | -6.1% |
| **+20¢** | 28225 | 19658 | 8567 (173) | 4 | $-10662.61 | -6.0% |
| **+10¢ (15¢ stop)** | 61863 | 61764 | 99 (58) | 0 | $-22869.82 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 09:12 | +10 stop | HYPE | UP | 0.54 | 0.64 | 0.65 |
| 11-07 09:12 | +5 | HYPE | UP | 0.57 | 0.64 | 0.35 |
| 11-07 09:11 | +10 stop | HYPE | DOWN | 0.51 | 0.34 | -2.03 |
| 11-07 09:11 | +20 | HYPE | DOWN | 0.49 | open |  |
| 11-07 09:11 | +15 | HYPE | DOWN | 0.49 | open |  |
| 11-07 09:11 | +10 | HYPE | DOWN | 0.49 | open |  |
| 11-07 09:11 | +5 | HYPE | DOWN | 0.49 | 0.58 | 0.54 |
| 11-07 09:08 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-07 09:08 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 11-07 09:08 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-07 09:08 | +5 | XRP | DOWN | 0.71 | 0.80 | 0.63 |
| 11-07 09:07 | +10 stop | DOGE | DOWN | 0.66 | 0.85 | 1.65 |
| 11-07 09:07 | +20 | DOGE | DOWN | 0.66 | 0.91 | 2.28 |
| 11-07 09:07 | +15 | DOGE | DOWN | 0.66 | 0.85 | 1.65 |
| 11-07 09:07 | +10 | DOGE | DOWN | 0.66 | 0.85 | 1.65 |
| 11-07 09:07 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-07 09:05 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 11-07 09:04 | +10 stop | HYPE | UP | 0.71 | 0.81 | 0.74 |
| 11-07 09:03 | +10 stop | XRP | DOWN | 0.57 | 0.73 | 1.28 |
| 11-07 09:03 | +20 | XRP | DOWN | 0.57 | 0.80 | 2.00 |
| 11-07 09:03 | +15 | XRP | DOWN | 0.57 | 0.73 | 1.28 |
| 11-07 09:03 | +10 | XRP | DOWN | 0.57 | 0.73 | 1.28 |
| 11-07 09:03 | +5 | XRP | DOWN | 0.57 | 0.64 | 0.35 |
| 11-07 09:02 | +5 | HYPE | DOWN | 0.63 | 0.71 | 0.48 |
| 11-07 09:02 | +10 stop | BTC | DOWN | 0.68 | 0.87 | 1.66 |
| 11-07 09:02 | +15 | BTC | DOWN | 0.68 | 0.87 | 1.66 |
| 11-07 09:02 | +10 | BTC | DOWN | 0.68 | 0.87 | 1.66 |
| 11-07 09:02 | +10 stop | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-07 09:02 | +20 | BNB | DOWN | 0.68 | open |  |
| 11-07 09:02 | +15 | BNB | DOWN | 0.68 | 0.85 | 1.45 |
| 11-07 09:02 | +10 | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-07 09:02 | +5 | BNB | DOWN | 0.68 | 0.74 | 0.30 |
| 11-07 09:02 | +5 | BTC | DOWN | 0.70 | 0.87 | 1.47 |
| 11-07 09:02 | +10 stop | ZEC | UP | 0.48 | 0.72 | 2.07 |
| 11-07 09:02 | +10 stop | HYPE | DOWN | 0.56 | 0.38 | -2.15 |
| 11-07 09:02 | +5 | HYPE | DOWN | 0.56 | 0.63 | 0.35 |
| 11-07 09:01 | +10 stop | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 11-07 09:01 | +20 | NEAR | DOWN | 0.68 | 0.88 | 1.76 |
| 11-07 09:01 | +15 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 11-07 09:01 | +10 stop | ETH | DOWN | 0.67 | 0.81 | 1.13 |
