# Range-Scalp Bot

*Updated Mon Oct 05 12:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3774 | 3246 | 528 (3) | 2 | $-1329.73 | -5.6% |
| **+10¢** | 2920 | 2313 | 607 (4) | 2 | $-1202.55 | -6.5% |
| **+15¢** | 2452 | 1814 | 638 (7) | 3 | $-1031.84 | -6.7% |
| **+20¢** | 2190 | 1524 | 666 (12) | 5 | $-877.42 | -6.4% |
| **+10¢ (15¢ stop)** | 4667 | 4666 | 1 (1) | 1 | $-1756.67 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 12:04 | +5 | XRP | DOWN | 0.70 | open |  |
| 10-05 12:03 | +5 | BTC | DOWN | 0.71 | 0.79 | 0.53 |
| 10-05 12:03 | +10 stop | XRP | DOWN | 0.65 | open |  |
| 10-05 12:02 | +10 stop | XRP | DOWN | 0.48 | 0.60 | 0.85 |
| 10-05 12:02 | +10 stop | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 10-05 12:02 | +20 | NEAR | DOWN | 0.67 | open |  |
| 10-05 12:02 | +15 | NEAR | DOWN | 0.67 | 0.84 | 1.44 |
| 10-05 12:02 | +10 | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 10-05 12:02 | +5 | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 10-05 12:01 | +10 stop | DOGE | DOWN | 0.66 | 0.78 | 0.88 |
| 10-05 12:01 | +20 | DOGE | DOWN | 0.66 | 0.88 | 1.93 |
| 10-05 12:01 | +15 | DOGE | DOWN | 0.66 | 0.82 | 1.30 |
| 10-05 12:01 | +10 | DOGE | DOWN | 0.66 | 0.78 | 0.88 |
| 10-05 12:01 | +5 | DOGE | DOWN | 0.66 | 0.75 | 0.57 |
| 10-05 12:01 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-05 12:01 | +20 | BTC | DOWN | 0.69 | open |  |
| 10-05 12:01 | +15 | BTC | DOWN | 0.69 | open |  |
| 10-05 12:01 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-05 12:01 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-05 12:01 | +10 stop | ZEC | UP | 0.54 | 0.30 | -2.73 |
| 10-05 12:01 | +20 | ZEC | UP | 0.54 | open |  |
| 10-05 12:01 | +15 | ZEC | UP | 0.54 | open |  |
| 10-05 12:01 | +10 | ZEC | UP | 0.54 | open |  |
| 10-05 12:01 | +5 | ZEC | UP | 0.54 | open |  |
| 10-05 12:01 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-05 12:01 | +20 | HYPE | DOWN | 0.71 | open |  |
| 10-05 12:01 | +15 | HYPE | DOWN | 0.71 | 0.86 | 1.26 |
| 10-05 12:01 | +10 | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-05 12:01 | +5 | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-05 12:00 | +10 stop | XRP | DOWN | 0.64 | 0.48 | -1.95 |
| 10-05 12:00 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-05 12:00 | +15 | XRP | DOWN | 0.64 | open |  |
| 10-05 12:00 | +10 | XRP | DOWN | 0.64 | open |  |
| 10-05 12:00 | +5 | XRP | DOWN | 0.64 | 0.69 | 0.18 |
| 10-05 11:54 | +10 stop | BNB | DOWN | 0.66 | 0.50 | -1.94 |
| 10-05 11:53 | +10 stop | XRP | UP | 0.58 | 0.80 | 1.86 |
| 10-05 11:53 | +5 | NEAR | DOWN | 0.66 | yes | -6.75 |
| 10-05 11:53 | +10 stop | ETH | DOWN | 0.67 | 0.48 | -2.24 |
| 10-05 11:53 | +10 | ETH | DOWN | 0.67 | yes | -6.86 |
| 10-05 11:53 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
