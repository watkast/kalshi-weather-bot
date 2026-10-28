# Range-Scalp Bot

*Updated Wed Oct 28 00:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37275 | 32540 | 4735 (45) | 0 | $-10372.15 | -4.4% |
| **+10¢** | 27841 | 22355 | 5486 (67) | 0 | $-9271.62 | -5.3% |
| **+15¢** | 23296 | 17404 | 5892 (91) | 0 | $-8231.53 | -5.6% |
| **+20¢** | 20646 | 14481 | 6165 (116) | 0 | $-7194.78 | -5.5% |
| **+10¢ (15¢ stop)** | 45660 | 45595 | 65 (34) | 0 | $-17397.61 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 00:08 | +10 stop | HYPE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-28 00:08 | +10 | HYPE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-28 00:08 | +5 | HYPE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-28 00:06 | +10 stop | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-28 00:05 | +5 | BTC | DOWN | 0.53 | 0.58 | 0.14 |
| 10-28 00:04 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 10-28 00:04 | +20 | SOL | DOWN | 0.71 | 0.94 | 2.07 |
| 10-28 00:04 | +15 | SOL | DOWN | 0.71 | 0.86 | 1.26 |
| 10-28 00:04 | +10 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 10-28 00:04 | +5 | SOL | DOWN | 0.71 | 0.79 | 0.53 |
| 10-28 00:04 | +10 stop | HYPE | UP | 0.70 | 0.47 | -2.67 |
| 10-28 00:04 | +10 stop | BTC | DOWN | 0.67 | 0.52 | -1.84 |
| 10-28 00:04 | +20 | BTC | DOWN | 0.67 | 0.87 | 1.76 |
| 10-28 00:04 | +15 | BTC | DOWN | 0.67 | 0.84 | 1.44 |
| 10-28 00:04 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-28 00:04 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
| 10-28 00:04 | +10 stop | DOGE | DOWN | 0.69 | 0.86 | 1.46 |
| 10-28 00:04 | +10 | DOGE | DOWN | 0.69 | 0.86 | 1.46 |
| 10-28 00:04 | +5 | DOGE | DOWN | 0.69 | 0.77 | 0.52 |
| 10-28 00:02 | +10 stop | HYPE | DOWN | 0.59 | 0.36 | -2.64 |
| 10-28 00:02 | +20 | HYPE | DOWN | 0.60 | 0.80 | 1.71 |
| 10-28 00:02 | +15 | HYPE | DOWN | 0.60 | 0.76 | 1.30 |
| 10-28 00:02 | +10 | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-28 00:02 | +5 | HYPE | DOWN | 0.60 | 0.66 | 0.27 |
| 10-28 00:01 | +10 stop | BNB | DOWN | 0.70 | 0.83 | 1.05 |
| 10-28 00:01 | +20 | BNB | DOWN | 0.70 | 0.92 | 1.94 |
| 10-28 00:01 | +15 | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 10-28 00:01 | +10 | BNB | DOWN | 0.70 | 0.83 | 1.05 |
| 10-28 00:01 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 10-28 00:01 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-28 00:01 | +20 | DOGE | DOWN | 0.64 | 0.86 | 1.94 |
| 10-28 00:01 | +15 | DOGE | DOWN | 0.64 | 0.86 | 1.94 |
| 10-28 00:01 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-28 00:01 | +5 | DOGE | DOWN | 0.64 | 0.72 | 0.48 |
| 10-27 23:57 | +10 stop | BNB | DOWN | 0.52 | 0.31 | -2.43 |
| 10-27 23:57 | +10 stop | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 10-27 23:57 | +10 | ZEC | UP | 0.61 | 0.73 | 0.89 |
| 10-27 23:57 | +5 | ZEC | UP | 0.61 | 0.73 | 0.89 |
| 10-27 23:55 | +10 stop | ZEC | UP | 0.67 | 0.77 | 0.71 |
| 10-27 23:55 | +20 | ZEC | UP | 0.67 | no | -6.86 |
