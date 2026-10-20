# Range-Scalp Bot

*Updated Tue Oct 20 06:49 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25252 | 21986 | 3266 (31) | 2 | $-7390.51 | -4.6% |
| **+10¢** | 19005 | 15229 | 3776 (46) | 2 | $-6572.21 | -5.5% |
| **+15¢** | 15905 | 11837 | 4068 (70) | 5 | $-5927.54 | -5.9% |
| **+20¢** | 14059 | 9800 | 4259 (88) | 8 | $-5331.46 | -6.0% |
| **+10¢ (15¢ stop)** | 30968 | 30916 | 52 (30) | 2 | $-11480.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 06:49 | +10 stop | NEAR | DOWN | 0.61 | open |  |
| 10-20 06:48 | +10 stop | ETH | DOWN | 0.70 | open |  |
| 10-20 06:48 | +10 | ETH | DOWN | 0.70 | open |  |
| 10-20 06:48 | +5 | ETH | DOWN | 0.70 | open |  |
| 10-20 06:46 | +10 stop | NEAR | UP | 0.58 | 0.43 | -1.86 |
| 10-20 06:46 | +20 | NEAR | UP | 0.58 | open |  |
| 10-20 06:46 | +15 | NEAR | UP | 0.58 | open |  |
| 10-20 06:46 | +10 | NEAR | UP | 0.58 | open |  |
| 10-20 06:46 | +5 | NEAR | UP | 0.58 | open |  |
| 10-20 06:46 | +10 stop | ETH | DOWN | 0.58 | 0.70 | 0.87 |
| 10-20 06:46 | +20 | ETH | DOWN | 0.59 | open |  |
| 10-20 06:46 | +15 | ETH | DOWN | 0.59 | open |  |
| 10-20 06:46 | +10 | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 10-20 06:46 | +5 | ETH | DOWN | 0.58 | 0.70 | 0.87 |
| 10-20 06:46 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-20 06:46 | +20 | ZEC | DOWN | 0.67 | open |  |
| 10-20 06:46 | +15 | ZEC | DOWN | 0.67 | open |  |
| 10-20 06:46 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-20 06:46 | +5 | ZEC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-20 06:46 | +10 stop | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-20 06:46 | +20 | BTC | DOWN | 0.64 | open |  |
| 10-20 06:46 | +15 | BTC | DOWN | 0.64 | open |  |
| 10-20 06:46 | +10 | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-20 06:46 | +5 | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-20 06:46 | +10 stop | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-20 06:46 | +20 | DOGE | DOWN | 0.65 | open |  |
| 10-20 06:46 | +15 | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
| 10-20 06:46 | +10 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-20 06:46 | +5 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-20 06:46 | +10 stop | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 10-20 06:46 | +20 | SOL | DOWN | 0.65 | open |  |
| 10-20 06:46 | +15 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 10-20 06:46 | +10 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 10-20 06:46 | +5 | SOL | DOWN | 0.65 | 0.73 | 0.50 |
| 10-20 06:46 | +10 stop | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-20 06:46 | +20 | BNB | DOWN | 0.64 | open |  |
| 10-20 06:46 | +15 | BNB | DOWN | 0.64 | open |  |
| 10-20 06:46 | +10 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-20 06:46 | +5 | BNB | DOWN | 0.64 | 0.72 | 0.48 |
| 10-20 06:46 | +10 stop | XRP | DOWN | 0.66 | 0.79 | 1.02 |
