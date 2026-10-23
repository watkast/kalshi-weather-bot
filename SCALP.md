# Range-Scalp Bot

*Updated Fri Oct 23 13:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30383 | 26468 | 3915 (39) | 5 | $-8839.40 | -4.6% |
| **+10¢** | 22758 | 18228 | 4530 (56) | 6 | $-7901.17 | -5.5% |
| **+15¢** | 19046 | 14173 | 4873 (79) | 7 | $-7139.25 | -6.0% |
| **+20¢** | 16863 | 11757 | 5106 (102) | 8 | $-6427.50 | -6.1% |
| **+10¢ (15¢ stop)** | 37240 | 37181 | 59 (32) | 5 | $-14054.55 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 13:18 | +5 | XRP | DOWN | 0.55 | 0.64 | 0.55 |
| 10-23 13:18 | +10 stop | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-23 13:18 | +15 | ZEC | DOWN | 0.64 | open |  |
| 10-23 13:18 | +10 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-23 13:18 | +5 | ZEC | DOWN | 0.62 | 0.70 | 0.48 |
| 10-23 13:18 | +5 | XRP | DOWN | 0.59 | 0.66 | 0.37 |
| 10-23 13:18 | +5 | ETH | DOWN | 0.64 | open |  |
| 10-23 13:18 | +10 stop | HYPE | DOWN | 0.63 | 0.77 | 1.10 |
| 10-23 13:18 | +10 | HYPE | DOWN | 0.63 | 0.77 | 1.10 |
| 10-23 13:18 | +5 | HYPE | DOWN | 0.63 | 0.77 | 1.06 |
| 10-23 13:18 | +5 | SOL | DOWN | 0.58 | open |  |
| 10-23 13:17 | +10 stop | SOL | DOWN | 0.56 | open |  |
| 10-23 13:17 | +10 | SOL | DOWN | 0.56 | open |  |
| 10-23 13:17 | +5 | NEAR | DOWN | 0.71 | open |  |
| 10-23 13:17 | +5 | SOL | DOWN | 0.55 | 0.65 | 0.66 |
| 10-23 13:17 | +10 stop | BTC | DOWN | 0.53 | open |  |
| 10-23 13:17 | +20 | BTC | DOWN | 0.56 | open |  |
| 10-23 13:17 | +15 | BTC | DOWN | 0.59 | open |  |
| 10-23 13:17 | +10 | BTC | DOWN | 0.67 | open |  |
| 10-23 13:17 | +5 | BTC | DOWN | 0.67 | open |  |
| 10-23 13:17 | +10 stop | BNB | DOWN | 0.68 | 0.53 | -1.84 |
| 10-23 13:17 | +20 | BNB | DOWN | 0.68 | open |  |
| 10-23 13:17 | +15 | BNB | DOWN | 0.69 | open |  |
| 10-23 13:17 | +10 | BNB | DOWN | 0.69 | open |  |
| 10-23 13:17 | +5 | BNB | DOWN | 0.69 | open |  |
| 10-23 13:16 | +10 stop | NEAR | DOWN | 0.62 | open |  |
| 10-23 13:16 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-23 13:16 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-23 13:16 | +10 | NEAR | DOWN | 0.62 | open |  |
| 10-23 13:16 | +5 | NEAR | DOWN | 0.62 | 0.68 | 0.27 |
| 10-23 13:16 | +10 stop | XRP | DOWN | 0.64 | open |  |
| 10-23 13:16 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-23 13:16 | +15 | XRP | DOWN | 0.64 | open |  |
| 10-23 13:16 | +10 | XRP | DOWN | 0.63 | open |  |
| 10-23 13:16 | +5 | XRP | DOWN | 0.64 | 0.71 | 0.38 |
| 10-23 13:16 | +10 stop | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-23 13:16 | +20 | DOGE | DOWN | 0.65 | open |  |
| 10-23 13:16 | +15 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-23 13:16 | +10 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-23 13:16 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
