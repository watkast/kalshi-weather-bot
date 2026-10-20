# Range-Scalp Bot

*Updated Tue Oct 20 07:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25286 | 22015 | 3271 (31) | 2 | $-7406.21 | -4.6% |
| **+10¢** | 19029 | 15248 | 3781 (46) | 4 | $-6583.88 | -5.5% |
| **+15¢** | 15927 | 11854 | 4073 (70) | 4 | $-5932.22 | -5.9% |
| **+20¢** | 14078 | 9814 | 4264 (88) | 6 | $-5333.77 | -6.0% |
| **+10¢ (15¢ stop)** | 31021 | 30969 | 52 (30) | 3 | $-11510.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 07:19 | +10 stop | XRP | DOWN | 0.69 | open |  |
| 10-20 07:19 | +5 | XRP | DOWN | 0.69 | open |  |
| 10-20 07:19 | +10 stop | ETH | DOWN | 0.61 | open |  |
| 10-20 07:19 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-20 07:19 | +5 | ETH | DOWN | 0.61 | 0.68 | 0.37 |
| 10-20 07:19 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-20 07:18 | +10 stop | ETH | DOWN | 0.50 | 0.61 | 0.75 |
| 10-20 07:18 | +20 | ETH | DOWN | 0.51 | open |  |
| 10-20 07:18 | +15 | ETH | DOWN | 0.51 | 0.68 | 1.36 |
| 10-20 07:18 | +10 | ETH | DOWN | 0.51 | 0.61 | 0.65 |
| 10-20 07:18 | +5 | ETH | DOWN | 0.51 | 0.61 | 0.65 |
| 10-20 07:18 | +10 stop | DOGE | DOWN | 0.62 | open |  |
| 10-20 07:18 | +20 | DOGE | DOWN | 0.62 | open |  |
| 10-20 07:18 | +15 | DOGE | DOWN | 0.62 | open |  |
| 10-20 07:18 | +10 | DOGE | DOWN | 0.62 | open |  |
| 10-20 07:18 | +5 | DOGE | DOWN | 0.62 | 0.70 | 0.48 |
| 10-20 07:18 | +10 stop | SOL | DOWN | 0.70 | 0.50 | -2.33 |
| 10-20 07:18 | +20 | SOL | DOWN | 0.71 | open |  |
| 10-20 07:18 | +15 | SOL | DOWN | 0.71 | open |  |
| 10-20 07:18 | +10 | SOL | DOWN | 0.71 | open |  |
| 10-20 07:18 | +5 | SOL | DOWN | 0.71 | open |  |
| 10-20 07:18 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-20 07:18 | +20 | BTC | DOWN | 0.71 | open |  |
| 10-20 07:18 | +15 | BTC | DOWN | 0.71 | open |  |
| 10-20 07:18 | +10 | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-20 07:18 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-20 07:18 | +10 stop | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 10-20 07:18 | +20 | BNB | DOWN | 0.70 | open |  |
| 10-20 07:18 | +15 | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 10-20 07:18 | +10 | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 10-20 07:18 | +5 | BNB | DOWN | 0.70 | 0.76 | 0.32 |
| 10-20 07:16 | +10 stop | XRP | DOWN | 0.69 | 0.49 | -2.33 |
| 10-20 07:16 | +20 | XRP | DOWN | 0.69 | open |  |
| 10-20 07:16 | +15 | XRP | DOWN | 0.69 | open |  |
| 10-20 07:16 | +10 | XRP | DOWN | 0.69 | open |  |
| 10-20 07:16 | +5 | XRP | DOWN | 0.69 | 0.75 | 0.31 |
| 10-20 07:12 | +10 | XRP | UP | 0.70 | 0.98 | 2.60 |
| 10-20 07:12 | +10 stop | XRP | UP | 0.67 | 0.98 | 2.89 |
| 10-20 07:12 | +15 | XRP | UP | 0.69 | 0.98 | 2.70 |
| 10-20 07:12 | +5 | XRP | UP | 0.65 | 0.73 | 0.50 |
