# Range-Scalp Bot

*Updated Tue Nov 03 11:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45851 | 39927 | 5924 (69) | 5 | $-13205.18 | -4.6% |
| **+10¢** | 34240 | 27374 | 6866 (91) | 5 | $-12079.89 | -5.6% |
| **+15¢** | 28652 | 21266 | 7386 (119) | 5 | $-11063.95 | -6.2% |
| **+20¢** | 25448 | 17707 | 7741 (155) | 5 | $-9846.09 | -6.2% |
| **+10¢ (15¢ stop)** | 55940 | 55851 | 89 (53) | 0 | $-20979.36 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 11:27 | +10 stop | BTC | DOWN | 0.65 | 0.88 | 2.06 |
| 11-03 11:26 | +10 stop | ZEC | UP | 0.30 | 0.54 | 2.07 |
| 11-03 11:26 | +10 | ZEC | UP | 0.30 | 0.54 | 2.07 |
| 11-03 11:25 | +10 stop | ZEC | DOWN | 0.66 | 0.40 | -2.93 |
| 11-03 11:25 | +5 | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-03 11:25 | +10 stop | NEAR | DOWN | 0.67 | 0.42 | -2.84 |
| 11-03 11:25 | +20 | NEAR | DOWN | 0.67 | 0.91 | 2.14 |
| 11-03 11:25 | +15 | NEAR | DOWN | 0.67 | 0.85 | 1.55 |
| 11-03 11:25 | +10 | NEAR | DOWN | 0.67 | 0.85 | 1.55 |
| 11-03 11:25 | +5 | NEAR | DOWN | 0.67 | 0.75 | 0.50 |
| 11-03 11:19 | +10 stop | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
| 11-03 11:19 | +5 | ZEC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-03 11:19 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-03 11:18 | +10 stop | BNB | DOWN | 0.59 | 0.75 | 1.29 |
| 11-03 11:18 | +10 stop | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 11-03 11:18 | +5 | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-03 11:18 | +5 | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 11-03 11:17 | +10 stop | XRP | DOWN | 0.58 | 0.77 | 1.59 |
| 11-03 11:17 | +20 | XRP | DOWN | 0.58 | 0.80 | 1.90 |
| 11-03 11:17 | +15 | XRP | DOWN | 0.58 | 0.77 | 1.59 |
| 11-03 11:17 | +10 | XRP | DOWN | 0.58 | 0.77 | 1.59 |
| 11-03 11:17 | +5 | XRP | DOWN | 0.58 | 0.67 | 0.56 |
| 11-03 11:17 | +10 stop | DOGE | DOWN | 0.51 | 0.74 | 1.98 |
| 11-03 11:17 | +20 | DOGE | DOWN | 0.51 | 0.74 | 1.98 |
| 11-03 11:17 | +15 | DOGE | DOWN | 0.51 | 0.74 | 1.98 |
| 11-03 11:17 | +10 | DOGE | DOWN | 0.51 | 0.74 | 1.98 |
| 11-03 11:17 | +5 | DOGE | DOWN | 0.51 | 0.57 | 0.24 |
| 11-03 11:17 | +10 stop | HYPE | UP | 0.54 | 0.37 | -2.05 |
| 11-03 11:17 | +20 | HYPE | UP | 0.54 | open |  |
| 11-03 11:17 | +15 | HYPE | UP | 0.54 | open |  |
| 11-03 11:17 | +10 | HYPE | UP | 0.54 | open |  |
| 11-03 11:17 | +5 | HYPE | UP | 0.54 | open |  |
| 11-03 11:16 | +10 stop | ZEC | UP | 0.48 | 0.29 | -2.23 |
| 11-03 11:16 | +20 | ZEC | UP | 0.48 | 0.91 | 4.02 |
| 11-03 11:16 | +15 | ZEC | UP | 0.48 | 0.91 | 4.02 |
| 11-03 11:16 | +10 | ZEC | UP | 0.48 | 0.59 | 0.75 |
| 11-03 11:16 | +5 | ZEC | UP | 0.48 | 0.53 | 0.14 |
| 11-03 11:16 | +10 stop | SOL | UP | 0.55 | 0.28 | -3.03 |
| 11-03 11:16 | +20 | SOL | UP | 0.56 | open |  |
| 11-03 11:16 | +15 | SOL | UP | 0.56 | open |  |
