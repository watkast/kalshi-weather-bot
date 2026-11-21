# Range-Scalp Bot

*Updated Sat Nov 21 00:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66736 | 58242 | 8494 (128) | 2 | $-17951.17 | -4.3% |
| **+10¢** | 49834 | 39907 | 9927 (170) | 2 | $-16683.94 | -5.3% |
| **+15¢** | 41793 | 31091 | 10702 (217) | 3 | $-14980.05 | -5.7% |
| **+20¢** | 37204 | 25964 | 11240 (273) | 3 | $-13268.51 | -5.7% |
| **+10¢ (15¢ stop)** | 81270 | 81104 | 166 (100) | 0 | $-29999.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 00:13 | +10 stop | SOL | UP | 0.44 | 0.54 | 0.66 |
| 11-21 00:13 | +15 | SOL | UP | 0.44 | open |  |
| 11-21 00:13 | +10 | SOL | UP | 0.44 | 0.54 | 0.65 |
| 11-21 00:13 | +5 | SOL | UP | 0.44 | 0.54 | 0.64 |
| 11-21 00:11 | +10 stop | SOL | UP | 0.46 | 0.69 | 1.97 |
| 11-21 00:11 | +15 | SOL | UP | 0.46 | 0.69 | 1.97 |
| 11-21 00:11 | +10 | SOL | UP | 0.45 | 0.69 | 2.07 |
| 11-21 00:11 | +5 | SOL | UP | 0.45 | 0.69 | 2.07 |
| 11-21 00:10 | +10 stop | XRP | UP | 0.70 | 0.83 | 1.05 |
| 11-21 00:10 | +10 | XRP | UP | 0.70 | 0.83 | 1.05 |
| 11-21 00:10 | +5 | XRP | UP | 0.70 | 0.79 | 0.63 |
| 11-21 00:09 | +10 stop | SOL | UP | 0.63 | 0.73 | 0.69 |
| 11-21 00:09 | +15 | SOL | UP | 0.64 | 0.81 | 1.42 |
| 11-21 00:09 | +10 | SOL | UP | 0.63 | 0.73 | 0.69 |
| 11-21 00:09 | +5 | SOL | UP | 0.64 | 0.72 | 0.48 |
| 11-21 00:09 | +5 | BNB | UP | 0.71 | 0.77 | 0.32 |
| 11-21 00:08 | +10 stop | ZEC | DOWN | 0.67 | 0.84 | 1.44 |
| 11-21 00:08 | +10 stop | BNB | UP | 0.64 | 0.77 | 1.00 |
| 11-21 00:07 | +5 | BTC | UP | 0.70 | 0.77 | 0.42 |
| 11-21 00:07 | +10 stop | BTC | UP | 0.70 | 0.86 | 1.36 |
| 11-21 00:07 | +10 stop | SOL | UP | 0.68 | 0.80 | 0.92 |
| 11-21 00:07 | +10 stop | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-21 00:07 | +15 | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-21 00:07 | +10 | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-21 00:07 | +5 | HYPE | DOWN | 0.67 | 0.75 | 0.50 |
| 11-21 00:06 | +5 | XRP | UP | 0.70 | 0.76 | 0.32 |
| 11-21 00:05 | +10 stop | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-21 00:05 | +10 stop | BTC | DOWN | 0.55 | 0.39 | -1.95 |
| 11-21 00:04 | +5 | XRP | UP | 0.54 | 0.59 | 0.15 |
| 11-21 00:04 | +10 stop | SOL | UP | 0.55 | 0.67 | 0.86 |
| 11-21 00:04 | +10 stop | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-21 00:04 | +10 stop | DOGE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-21 00:04 | +10 stop | BNB | DOWN | 0.64 | 0.48 | -1.95 |
| 11-21 00:03 | +10 stop | BTC | DOWN | 0.55 | 0.39 | -1.95 |
| 11-21 00:03 | +10 stop | ZEC | DOWN | 0.60 | 0.70 | 0.69 |
| 11-21 00:02 | +5 | NEAR | DOWN | 0.62 | 0.75 | 0.99 |
| 11-21 00:02 | +10 stop | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
| 11-21 00:02 | +20 | HYPE | DOWN | 0.57 | 0.82 | 2.21 |
| 11-21 00:02 | +15 | HYPE | DOWN | 0.57 | 0.74 | 1.38 |
| 11-21 00:02 | +10 | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
