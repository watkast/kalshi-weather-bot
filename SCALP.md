# Range-Scalp Bot

*Updated Thu Oct 29 22:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39783 | 34739 | 5044 (50) | 0 | $-10987.91 | -4.4% |
| **+10¢** | 29661 | 23830 | 5831 (73) | 0 | $-9711.43 | -5.2% |
| **+15¢** | 24806 | 18531 | 6275 (100) | 0 | $-8727.70 | -5.6% |
| **+20¢** | 22013 | 15436 | 6577 (129) | 0 | $-7627.67 | -5.5% |
| **+10¢ (15¢ stop)** | 48581 | 48511 | 70 (37) | 0 | $-18389.53 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 22:13 | +5 | SOL | UP | 0.59 | no | -6.07 |
| 10-29 22:13 | +10 stop | HYPE | UP | 0.48 | 0.59 | 0.75 |
| 10-29 22:13 | +20 | HYPE | UP | 0.39 | 0.59 | 1.66 |
| 10-29 22:13 | +15 | HYPE | UP | 0.39 | 0.59 | 1.66 |
| 10-29 22:13 | +10 | HYPE | UP | 0.39 | 0.59 | 1.66 |
| 10-29 22:13 | +5 | HYPE | UP | 0.40 | 0.59 | 1.56 |
| 10-29 22:12 | +10 stop | SOL | DOWN | 0.46 | 0.94 | 4.56 |
| 10-29 22:12 | +20 | SOL | DOWN | 0.47 | 0.94 | 4.47 |
| 10-29 22:12 | +15 | SOL | DOWN | 0.47 | 0.94 | 4.47 |
| 10-29 22:12 | +10 | SOL | DOWN | 0.47 | 0.94 | 4.46 |
| 10-29 22:12 | +5 | SOL | DOWN | 0.47 | 0.53 | 0.24 |
| 10-29 22:12 | +10 stop | DOGE | UP | 0.64 | 0.25 | -4.26 |
| 10-29 22:12 | +20 | DOGE | UP | 0.63 | no | -6.47 |
| 10-29 22:12 | +15 | DOGE | UP | 0.61 | no | -6.27 |
| 10-29 22:12 | +10 | DOGE | UP | 0.58 | 0.72 | 1.07 |
| 10-29 22:12 | +5 | DOGE | UP | 0.61 | 0.66 | 0.17 |
| 10-29 22:04 | +5 | XRP | DOWN | 0.71 | 0.80 | 0.63 |
| 10-29 22:04 | +10 stop | HYPE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-29 22:04 | +10 stop | XRP | DOWN | 0.68 | 0.80 | 0.92 |
| 10-29 22:03 | +10 stop | XRP | UP | 0.66 | 0.43 | -2.59 |
| 10-29 22:03 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-29 22:02 | +10 stop | DOGE | DOWN | 0.56 | 0.41 | -1.85 |
| 10-29 22:01 | +10 stop | XRP | UP | 0.55 | 0.67 | 0.86 |
| 10-29 22:01 | +10 stop | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 10-29 22:01 | +20 | BNB | DOWN | 0.67 | 0.94 | 2.51 |
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
| 10-29 22:00 | +20 | XRP | DOWN | 0.63 | 0.83 | 1.73 |
| 10-29 22:00 | +15 | XRP | DOWN | 0.63 | 0.80 | 1.41 |
| 10-29 22:00 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-29 22:00 | +5 | XRP | DOWN | 0.63 | 0.69 | 0.28 |
| 10-29 22:00 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
