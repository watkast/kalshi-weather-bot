# Range-Scalp Bot

*Updated Mon Oct 19 16:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24251 | 21090 | 3161 (31) | 7 | $-7216.71 | -4.7% |
| **+10¢** | 18235 | 14585 | 3650 (46) | 8 | $-6460.98 | -5.6% |
| **+15¢** | 15279 | 11349 | 3930 (69) | 8 | $-5844.20 | -6.1% |
| **+20¢** | 13522 | 9408 | 4114 (87) | 8 | $-5247.60 | -6.2% |
| **+10¢ (15¢ stop)** | 29848 | 29796 | 52 (30) | 3 | $-11339.67 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 16:32 | +10 stop | ZEC | DOWN | 0.62 | open |  |
| 10-19 16:32 | +20 | ZEC | DOWN | 0.62 | open |  |
| 10-19 16:32 | +15 | ZEC | DOWN | 0.62 | open |  |
| 10-19 16:32 | +10 | ZEC | DOWN | 0.62 | open |  |
| 10-19 16:32 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 10-19 16:31 | +10 stop | SOL | DOWN | 0.71 | 0.53 | -2.13 |
| 10-19 16:31 | +20 | SOL | DOWN | 0.70 | open |  |
| 10-19 16:31 | +15 | SOL | DOWN | 0.70 | open |  |
| 10-19 16:31 | +10 | SOL | DOWN | 0.69 | open |  |
| 10-19 16:31 | +5 | SOL | DOWN | 0.69 | open |  |
| 10-19 16:31 | +10 stop | ETH | DOWN | 0.62 | 0.44 | -2.15 |
| 10-19 16:31 | +20 | ETH | DOWN | 0.62 | open |  |
| 10-19 16:31 | +15 | ETH | DOWN | 0.62 | open |  |
| 10-19 16:31 | +10 | ETH | DOWN | 0.62 | open |  |
| 10-19 16:31 | +5 | ETH | DOWN | 0.62 | open |  |
| 10-19 16:31 | +10 stop | XRP | DOWN | 0.68 | 0.48 | -2.34 |
| 10-19 16:31 | +20 | XRP | DOWN | 0.68 | open |  |
| 10-19 16:31 | +15 | XRP | DOWN | 0.68 | open |  |
| 10-19 16:31 | +10 | XRP | DOWN | 0.67 | open |  |
| 10-19 16:31 | +5 | XRP | DOWN | 0.67 | open |  |
| 10-19 16:31 | +10 stop | BTC | DOWN | 0.67 | 0.51 | -1.94 |
| 10-19 16:31 | +20 | BTC | DOWN | 0.67 | open |  |
| 10-19 16:31 | +15 | BTC | DOWN | 0.67 | open |  |
| 10-19 16:31 | +10 | BTC | DOWN | 0.66 | open |  |
| 10-19 16:31 | +5 | BTC | DOWN | 0.66 | open |  |
| 10-19 16:31 | +10 stop | HYPE | DOWN | 0.68 | open |  |
| 10-19 16:31 | +20 | HYPE | DOWN | 0.68 | open |  |
| 10-19 16:31 | +15 | HYPE | DOWN | 0.68 | open |  |
| 10-19 16:31 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-19 16:31 | +5 | HYPE | DOWN | 0.67 | open |  |
| 10-19 16:31 | +10 stop | BNB | DOWN | 0.63 | open |  |
| 10-19 16:31 | +20 | BNB | DOWN | 0.64 | open |  |
| 10-19 16:31 | +15 | BNB | DOWN | 0.64 | open |  |
| 10-19 16:31 | +10 | BNB | DOWN | 0.65 | open |  |
| 10-19 16:31 | +5 | BNB | DOWN | 0.63 | open |  |
| 10-19 16:30 | +10 stop | DOGE | DOWN | 0.70 | 0.52 | -2.13 |
| 10-19 16:30 | +20 | DOGE | DOWN | 0.70 | open |  |
| 10-19 16:30 | +15 | DOGE | DOWN | 0.70 | open |  |
| 10-19 16:30 | +10 | DOGE | DOWN | 0.70 | open |  |
| 10-19 16:30 | +5 | DOGE | DOWN | 0.70 | open |  |
