# Range-Scalp Bot

*Updated Fri Oct 23 12:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30290 | 26381 | 3909 (39) | 0 | $-8843.92 | -4.6% |
| **+10¢** | 22702 | 18180 | 4522 (56) | 0 | $-7899.55 | -5.5% |
| **+15¢** | 19005 | 14142 | 4863 (79) | 0 | $-7125.91 | -6.0% |
| **+20¢** | 16825 | 11730 | 5095 (102) | 1 | $-6412.55 | -6.1% |
| **+10¢ (15¢ stop)** | 37152 | 37093 | 59 (32) | 0 | $-14033.86 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 12:06 | +10 stop | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 10-23 12:06 | +20 | SOL | DOWN | 0.70 | 0.92 | 1.98 |
| 10-23 12:06 | +15 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 10-23 12:06 | +10 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 10-23 12:06 | +5 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 10-23 12:06 | +10 stop | DOGE | DOWN | 0.69 | 0.88 | 1.67 |
| 10-23 12:06 | +10 | DOGE | DOWN | 0.69 | 0.88 | 1.67 |
| 10-23 12:06 | +5 | DOGE | DOWN | 0.69 | 0.75 | 0.31 |
| 10-23 12:05 | +10 stop | BNB | DOWN | 0.67 | 0.47 | -2.34 |
| 10-23 12:04 | +5 | HYPE | DOWN | 0.68 | 0.77 | 0.57 |
| 10-23 12:04 | +10 stop | BNB | UP | 0.46 | 0.59 | 0.95 |
| 10-23 12:04 | +10 stop | HYPE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-23 12:04 | +20 | HYPE | DOWN | 0.58 | 0.81 | 2.01 |
| 10-23 12:04 | +15 | HYPE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-23 12:04 | +10 | HYPE | DOWN | 0.59 | 0.71 | 0.88 |
| 10-23 12:04 | +5 | HYPE | DOWN | 0.60 | 0.65 | 0.17 |
| 10-23 12:03 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-23 12:03 | +20 | BTC | DOWN | 0.67 | 0.91 | 2.22 |
| 10-23 12:03 | +15 | BTC | DOWN | 0.67 | 0.84 | 1.44 |
| 10-23 12:03 | +10 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-23 12:03 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
| 10-23 12:03 | +10 stop | XRP | DOWN | 0.65 | 0.88 | 2.06 |
| 10-23 12:03 | +10 | XRP | DOWN | 0.65 | 0.88 | 2.06 |
| 10-23 12:03 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 10-23 12:02 | +10 stop | BNB | DOWN | 0.63 | 0.48 | -1.85 |
| 10-23 12:02 | +20 | BNB | DOWN | 0.63 | open |  |
| 10-23 12:02 | +15 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-23 12:02 | +10 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-23 12:02 | +5 | BNB | DOWN | 0.63 | 0.71 | 0.48 |
| 10-23 12:01 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-23 12:01 | +20 | DOGE | DOWN | 0.62 | 0.88 | 2.35 |
| 10-23 12:01 | +15 | DOGE | DOWN | 0.62 | 0.88 | 2.35 |
| 10-23 12:01 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-23 12:01 | +5 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-23 12:01 | +10 stop | XRP | DOWN | 0.65 | 0.77 | 0.92 |
| 10-23 12:01 | +20 | XRP | DOWN | 0.65 | 0.88 | 2.07 |
| 10-23 12:01 | +15 | XRP | DOWN | 0.65 | 0.88 | 2.07 |
| 10-23 12:01 | +10 | XRP | DOWN | 0.65 | 0.77 | 0.92 |
| 10-23 12:01 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.30 |
| 10-23 11:58 | +10 stop | BTC | DOWN | 0.71 | 0.87 | 1.37 |
