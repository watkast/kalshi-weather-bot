# Range-Scalp Bot

*Updated Thu Nov 12 13:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56932 | 49631 | 7301 (101) | 3 | $-15656.10 | -4.4% |
| **+10¢** | 42544 | 34028 | 8516 (133) | 6 | $-14577.80 | -5.5% |
| **+15¢** | 35669 | 26502 | 9167 (167) | 7 | $-13187.01 | -5.9% |
| **+20¢** | 31776 | 22158 | 9618 (217) | 8 | $-11564.10 | -5.8% |
| **+10¢ (15¢ stop)** | 69396 | 69268 | 128 (78) | 3 | $-25636.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 13:05 | +10 stop | NEAR | DOWN | 0.61 | open |  |
| 11-12 13:05 | +10 stop | BTC | DOWN | 0.63 | open |  |
| 11-12 13:05 | +5 | NEAR | DOWN | 0.67 | open |  |
| 11-12 13:04 | +5 | BNB | UP | 0.46 | 0.56 | 0.64 |
| 11-12 13:04 | +5 | XRP | DOWN | 0.62 | 0.77 | 1.20 |
| 11-12 13:04 | +10 stop | HYPE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-12 13:04 | +10 stop | NEAR | DOWN | 0.49 | 0.65 | 1.26 |
| 11-12 13:04 | +5 | NEAR | DOWN | 0.49 | 0.57 | 0.44 |
| 11-12 13:03 | +10 stop | BNB | UP | 0.61 | 0.42 | -2.25 |
| 11-12 13:03 | +10 | BNB | UP | 0.61 | open |  |
| 11-12 13:03 | +5 | BNB | UP | 0.61 | 0.69 | 0.48 |
| 11-12 13:03 | +10 stop | NEAR | UP | 0.42 | 0.57 | 1.14 |
| 11-12 13:03 | +5 | NEAR | UP | 0.46 | 0.57 | 0.74 |
| 11-12 13:03 | +10 stop | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 13:03 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-12 13:03 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-12 13:03 | +10 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 13:03 | +5 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 13:03 | +10 stop | BTC | UP | 0.58 | 0.37 | -2.45 |
| 11-12 13:03 | +20 | BTC | UP | 0.58 | open |  |
| 11-12 13:03 | +15 | BTC | UP | 0.59 | open |  |
| 11-12 13:03 | +10 | BTC | UP | 0.59 | open |  |
| 11-12 13:03 | +5 | BTC | UP | 0.59 | open |  |
| 11-12 13:03 | +10 | SOL | DOWN | 0.56 | 0.66 | 0.66 |
| 11-12 13:02 | +5 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 11-12 13:02 | +10 stop | DOGE | DOWN | 0.69 | open |  |
| 11-12 13:02 | +5 | DOGE | DOWN | 0.69 | 0.77 | 0.52 |
| 11-12 13:02 | +10 stop | BNB | UP | 0.55 | 0.68 | 0.96 |
| 11-12 13:02 | +20 | BNB | UP | 0.55 | open |  |
| 11-12 13:02 | +15 | BNB | UP | 0.55 | open |  |
| 11-12 13:02 | +10 | BNB | UP | 0.55 | 0.68 | 0.96 |
| 11-12 13:02 | +5 | BNB | UP | 0.55 | 0.68 | 0.96 |
| 11-12 13:01 | +10 stop | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 11-12 13:01 | +20 | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 11-12 13:01 | +15 | SOL | DOWN | 0.57 | 0.78 | 1.79 |
| 11-12 13:01 | +10 | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 11-12 13:01 | +5 | SOL | DOWN | 0.57 | 0.63 | 0.25 |
| 11-12 13:01 | +10 stop | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-12 13:01 | +20 | ETH | DOWN | 0.68 | open |  |
| 11-12 13:01 | +15 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
