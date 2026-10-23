# Range-Scalp Bot

*Updated Fri Oct 23 12:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30300 | 26391 | 3909 (39) | 2 | $-8836.77 | -4.6% |
| **+10¢** | 22710 | 18188 | 4522 (56) | 3 | $-7890.79 | -5.5% |
| **+15¢** | 19009 | 14146 | 4863 (79) | 4 | $-7118.06 | -6.0% |
| **+20¢** | 16830 | 11735 | 5095 (102) | 4 | $-6402.51 | -6.1% |
| **+10¢ (15¢ stop)** | 37164 | 37105 | 59 (32) | 0 | $-14035.45 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 12:27 | +10 stop | BNB | UP | 0.51 | 0.63 | 0.85 |
| 10-23 12:27 | +10 | BNB | UP | 0.51 | 0.63 | 0.85 |
| 10-23 12:27 | +5 | BNB | UP | 0.51 | 0.63 | 0.85 |
| 10-23 12:22 | +10 stop | BNB | UP | 0.67 | 0.78 | 0.81 |
| 10-23 12:22 | +10 | BNB | UP | 0.67 | 0.78 | 0.81 |
| 10-23 12:22 | +5 | BNB | UP | 0.67 | 0.78 | 0.81 |
| 10-23 12:21 | +5 | BNB | UP | 0.54 | 0.59 | 0.15 |
| 10-23 12:20 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 10-23 12:19 | +10 stop | BNB | UP | 0.51 | 0.66 | 1.16 |
| 10-23 12:19 | +10 | BNB | UP | 0.52 | 0.66 | 1.06 |
| 10-23 12:19 | +5 | BNB | UP | 0.52 | 0.59 | 0.35 |
| 10-23 12:18 | +10 stop | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 10-23 12:18 | +20 | DOGE | UP | 0.70 | 0.91 | 1.83 |
| 10-23 12:18 | +15 | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 10-23 12:18 | +10 | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 10-23 12:18 | +5 | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 10-23 12:16 | +10 stop | XRP | DOWN | 0.57 | 0.32 | -2.84 |
| 10-23 12:16 | +20 | XRP | DOWN | 0.57 | open |  |
| 10-23 12:16 | +15 | XRP | DOWN | 0.57 | open |  |
| 10-23 12:16 | +10 | XRP | DOWN | 0.57 | open |  |
| 10-23 12:16 | +5 | XRP | DOWN | 0.57 | open |  |
| 10-23 12:16 | +10 stop | NEAR | UP | 0.57 | 0.71 | 1.07 |
| 10-23 12:16 | +20 | NEAR | UP | 0.57 | 0.82 | 2.21 |
| 10-23 12:16 | +15 | NEAR | UP | 0.58 | 0.82 | 2.11 |
| 10-23 12:16 | +10 | NEAR | UP | 0.58 | 0.71 | 0.97 |
| 10-23 12:16 | +5 | NEAR | UP | 0.58 | 0.71 | 0.97 |
| 10-23 12:16 | +10 stop | BTC | DOWN | 0.64 | 0.48 | -1.95 |
| 10-23 12:16 | +20 | BTC | DOWN | 0.64 | open |  |
| 10-23 12:16 | +15 | BTC | DOWN | 0.64 | open |  |
| 10-23 12:16 | +10 | BTC | DOWN | 0.64 | open |  |
| 10-23 12:16 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-23 12:16 | +10 stop | SOL | UP | 0.63 | 0.76 | 1.02 |
| 10-23 12:16 | +20 | SOL | UP | 0.63 | 0.86 | 2.06 |
| 10-23 12:16 | +15 | SOL | UP | 0.63 | 0.86 | 2.06 |
| 10-23 12:16 | +10 | SOL | UP | 0.63 | 0.76 | 1.02 |
| 10-23 12:16 | +5 | SOL | UP | 0.63 | 0.69 | 0.30 |
| 10-23 12:16 | +10 stop | ZEC | UP | 0.57 | 0.39 | -2.15 |
| 10-23 12:16 | +20 | ZEC | UP | 0.57 | 0.81 | 2.11 |
| 10-23 12:16 | +15 | ZEC | UP | 0.57 | 0.81 | 2.11 |
| 10-23 12:16 | +10 | ZEC | UP | 0.57 | 0.81 | 2.11 |
