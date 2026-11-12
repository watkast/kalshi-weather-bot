# Range-Scalp Bot

*Updated Thu Nov 12 20:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57225 | 49892 | 7333 (101) | 2 | $-15705.95 | -4.4% |
| **+10¢** | 42773 | 34214 | 8559 (133) | 5 | $-14646.57 | -5.4% |
| **+15¢** | 35860 | 26647 | 9213 (167) | 6 | $-13243.48 | -5.9% |
| **+20¢** | 31949 | 22283 | 9666 (217) | 7 | $-11600.46 | -5.8% |
| **+10¢ (15¢ stop)** | 69771 | 69643 | 128 (78) | 2 | $-25720.48 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 20:20 | +5 | BNB | DOWN | 0.60 | open |  |
| 11-12 20:20 | +10 stop | ETH | UP | 0.55 | 0.70 | 1.17 |
| 11-12 20:20 | +20 | ETH | UP | 0.55 | open |  |
| 11-12 20:20 | +15 | ETH | UP | 0.55 | 0.70 | 1.17 |
| 11-12 20:20 | +10 | ETH | UP | 0.56 | 0.70 | 1.07 |
| 11-12 20:20 | +5 | ETH | UP | 0.56 | 0.70 | 1.07 |
| 11-12 20:19 | +10 stop | BNB | DOWN | 0.59 | open |  |
| 11-12 20:19 | +20 | BNB | DOWN | 0.59 | open |  |
| 11-12 20:19 | +15 | BNB | DOWN | 0.60 | open |  |
| 11-12 20:19 | +10 | BNB | DOWN | 0.61 | open |  |
| 11-12 20:19 | +5 | BNB | DOWN | 0.62 | 0.68 | 0.27 |
| 11-12 20:19 | +5 | DOGE | UP | 0.65 | 0.73 | 0.50 |
| 11-12 20:19 | +10 stop | HYPE | UP | 0.70 | open |  |
| 11-12 20:19 | +5 | HYPE | UP | 0.70 | 0.75 | 0.21 |
| 11-12 20:19 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-12 20:19 | +20 | ZEC | DOWN | 0.61 | open |  |
| 11-12 20:19 | +15 | ZEC | DOWN | 0.59 | open |  |
| 11-12 20:19 | +10 | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 11-12 20:19 | +5 | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 11-12 20:18 | +10 stop | DOGE | DOWN | 0.59 | 0.41 | -2.14 |
| 11-12 20:18 | +15 | DOGE | DOWN | 0.60 | open |  |
| 11-12 20:18 | +10 | DOGE | DOWN | 0.60 | open |  |
| 11-12 20:18 | +5 | DOGE | DOWN | 0.60 | 0.65 | 0.17 |
| 11-12 20:18 | +10 stop | SOL | DOWN | 0.60 | 0.31 | -3.22 |
| 11-12 20:18 | +15 | SOL | DOWN | 0.60 | open |  |
| 11-12 20:18 | +10 | SOL | DOWN | 0.60 | open |  |
| 11-12 20:18 | +5 | SOL | DOWN | 0.60 | open |  |
| 11-12 20:17 | +5 | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 11-12 20:17 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-12 20:17 | +10 stop | XRP | DOWN | 0.65 | 0.44 | -2.44 |
| 11-12 20:17 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-12 20:17 | +5 | XRP | DOWN | 0.64 | 0.69 | 0.18 |
| 11-12 20:17 | +10 stop | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-12 20:17 | +20 | NEAR | DOWN | 0.60 | open |  |
| 11-12 20:17 | +15 | NEAR | DOWN | 0.60 | open |  |
| 11-12 20:17 | +10 | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-12 20:17 | +5 | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-12 20:16 | +10 stop | DOGE | DOWN | 0.56 | 0.69 | 0.97 |
| 11-12 20:16 | +20 | DOGE | DOWN | 0.56 | open |  |
| 11-12 20:16 | +15 | DOGE | DOWN | 0.56 | 0.72 | 1.27 |
