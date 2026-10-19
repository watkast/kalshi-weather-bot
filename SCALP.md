# Range-Scalp Bot

*Updated Mon Oct 19 21:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24631 | 21441 | 3190 (31) | 1 | $-7208.38 | -4.6% |
| **+10¢** | 18519 | 14834 | 3685 (46) | 1 | $-6419.52 | -5.5% |
| **+15¢** | 15509 | 11541 | 3968 (70) | 1 | $-5772.06 | -5.9% |
| **+20¢** | 13714 | 9558 | 4156 (88) | 5 | $-5199.02 | -6.0% |
| **+10¢ (15¢ stop)** | 30269 | 30217 | 52 (30) | 0 | $-11388.51 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 21:48 | +5 | BNB | DOWN | 0.66 | 0.78 | 0.91 |
| 10-19 21:47 | +5 | HYPE | DOWN | 0.58 | 0.67 | 0.52 |
| 10-19 21:47 | +10 stop | ZEC | UP | 0.55 | 0.25 | -3.32 |
| 10-19 21:47 | +20 | ZEC | UP | 0.55 | open |  |
| 10-19 21:47 | +15 | ZEC | UP | 0.55 | open |  |
| 10-19 21:47 | +10 | ZEC | UP | 0.55 | open |  |
| 10-19 21:47 | +5 | ZEC | UP | 0.55 | open |  |
| 10-19 21:47 | +10 stop | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 10-19 21:47 | +20 | ETH | DOWN | 0.68 | 0.92 | 2.17 |
| 10-19 21:47 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-19 21:47 | +10 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 10-19 21:47 | +5 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 10-19 21:46 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 10-19 21:46 | +20 | SOL | DOWN | 0.71 | open |  |
| 10-19 21:46 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 10-19 21:46 | +10 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 10-19 21:46 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 10-19 21:46 | +10 stop | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 10-19 21:46 | +20 | BNB | DOWN | 0.62 | open |  |
| 10-19 21:46 | +15 | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 10-19 21:46 | +10 | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 10-19 21:46 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 10-19 21:46 | +10 stop | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-19 21:46 | +20 | DOGE | DOWN | 0.63 | 0.83 | 1.73 |
| 10-19 21:46 | +15 | DOGE | DOWN | 0.63 | 0.83 | 1.73 |
| 10-19 21:46 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-19 21:46 | +5 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-19 21:46 | +10 stop | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 10-19 21:46 | +20 | XRP | DOWN | 0.69 | open |  |
| 10-19 21:46 | +15 | XRP | DOWN | 0.69 | 0.87 | 1.57 |
| 10-19 21:46 | +10 | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 10-19 21:46 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 10-19 21:46 | +10 stop | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 10-19 21:46 | +20 | HYPE | DOWN | 0.55 | 0.75 | 1.68 |
| 10-19 21:46 | +15 | HYPE | DOWN | 0.55 | 0.70 | 1.17 |
| 10-19 21:46 | +10 | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-19 21:46 | +5 | HYPE | DOWN | 0.56 | 0.61 | 0.15 |
| 10-19 21:46 | +10 stop | BTC | DOWN | 0.71 | 0.84 | 1.05 |
| 10-19 21:46 | +20 | BTC | DOWN | 0.71 | open |  |
| 10-19 21:46 | +15 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
