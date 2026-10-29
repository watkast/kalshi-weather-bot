# Range-Scalp Bot

*Updated Thu Oct 29 22:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39779 | 34736 | 5043 (50) | 0 | $-10983.81 | -4.4% |
| **+10¢** | 29658 | 23827 | 5831 (73) | 0 | $-9718.62 | -5.2% |
| **+15¢** | 24802 | 18528 | 6274 (100) | 1 | $-8728.99 | -5.6% |
| **+20¢** | 22007 | 15431 | 6576 (129) | 3 | $-7633.63 | -5.5% |
| **+10¢ (15¢ stop)** | 48577 | 48507 | 70 (37) | 1 | $-18391.40 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 22:04 | +5 | XRP | DOWN | 0.71 | 0.80 | 0.63 |
| 10-29 22:04 | +10 stop | HYPE | DOWN | 0.68 | open |  |
| 10-29 22:04 | +10 stop | XRP | DOWN | 0.68 | 0.80 | 0.92 |
| 10-29 22:03 | +10 stop | XRP | UP | 0.66 | 0.43 | -2.59 |
| 10-29 22:03 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-29 22:02 | +10 stop | DOGE | DOWN | 0.56 | 0.41 | -1.85 |
| 10-29 22:01 | +10 stop | XRP | UP | 0.55 | 0.67 | 0.86 |
| 10-29 22:01 | +10 stop | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 10-29 22:01 | +20 | BNB | DOWN | 0.67 | open |  |
| 10-29 22:01 | +15 | BNB | DOWN | 0.67 | 0.83 | 1.34 |
| 10-29 22:01 | +10 | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 10-29 22:01 | +5 | BNB | DOWN | 0.67 | 0.74 | 0.40 |
| 10-29 22:01 | +5 | NEAR | DOWN | 0.64 | 0.76 | 0.86 |
| 10-29 22:01 | +10 stop | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-29 22:01 | +20 | SOL | DOWN | 0.68 | 0.91 | 2.04 |
| 10-29 22:01 | +15 | SOL | DOWN | 0.68 | 0.86 | 1.55 |
| 10-29 22:01 | +10 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-29 22:01 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 10-29 22:00 | +10 stop | XRP | DOWN | 0.63 | 0.39 | -2.74 |
| 10-29 22:00 | +20 | XRP | DOWN | 0.63 | open |  |
| 10-29 22:00 | +15 | XRP | DOWN | 0.63 | 0.80 | 1.41 |
| 10-29 22:00 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-29 22:00 | +5 | XRP | DOWN | 0.63 | 0.69 | 0.28 |
| 10-29 22:00 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 22:00 | +20 | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 10-29 22:00 | +15 | BTC | DOWN | 0.63 | 0.84 | 1.83 |
| 10-29 22:00 | +10 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-29 22:00 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-29 22:00 | +10 stop | DOGE | DOWN | 0.64 | 0.48 | -1.95 |
| 10-29 22:00 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 10-29 22:00 | +15 | DOGE | DOWN | 0.64 | 0.80 | 1.31 |
| 10-29 22:00 | +10 | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-29 22:00 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 10-29 22:00 | +10 stop | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 10-29 22:00 | +20 | NEAR | DOWN | 0.63 | 0.84 | 1.83 |
| 10-29 22:00 | +15 | NEAR | DOWN | 0.63 | 0.80 | 1.41 |
| 10-29 22:00 | +10 | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 10-29 22:00 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 10-29 22:00 | +10 stop | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-29 22:00 | +20 | ZEC | DOWN | 0.62 | 0.82 | 1.72 |
