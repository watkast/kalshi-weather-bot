# Range-Scalp Bot

*Updated Sat Oct 24 15:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32158 | 28035 | 4123 (40) | 2 | $-9214.06 | -4.5% |
| **+10¢** | 24073 | 19301 | 4772 (58) | 3 | $-8241.85 | -5.4% |
| **+15¢** | 20155 | 15022 | 5133 (81) | 3 | $-7386.26 | -5.8% |
| **+20¢** | 17857 | 12484 | 5373 (103) | 3 | $-6556.77 | -5.8% |
| **+10¢ (15¢ stop)** | 39529 | 39470 | 59 (32) | 3 | $-15146.30 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 15:19 | +10 | HYPE | DOWN | 0.56 | open |  |
| 10-24 15:18 | +15 | NEAR | DOWN | 0.61 | open |  |
| 10-24 15:18 | +10 | HYPE | DOWN | 0.54 | 0.66 | 0.86 |
| 10-24 15:18 | +10 stop | NEAR | DOWN | 0.67 | open |  |
| 10-24 15:18 | +10 | NEAR | DOWN | 0.67 | open |  |
| 10-24 15:18 | +5 | NEAR | DOWN | 0.67 | open |  |
| 10-24 15:17 | +5 | HYPE | DOWN | 0.70 | open |  |
| 10-24 15:17 | +10 stop | HYPE | DOWN | 0.62 | open |  |
| 10-24 15:17 | +20 | HYPE | DOWN | 0.62 | open |  |
| 10-24 15:17 | +15 | HYPE | DOWN | 0.63 | open |  |
| 10-24 15:17 | +10 | HYPE | DOWN | 0.60 | 0.71 | 0.76 |
| 10-24 15:17 | +5 | HYPE | DOWN | 0.60 | 0.66 | 0.25 |
| 10-24 15:17 | +10 stop | NEAR | DOWN | 0.50 | 0.62 | 0.85 |
| 10-24 15:17 | +20 | NEAR | DOWN | 0.50 | open |  |
| 10-24 15:17 | +15 | NEAR | DOWN | 0.50 | 0.66 | 1.26 |
| 10-24 15:17 | +10 | NEAR | DOWN | 0.51 | 0.62 | 0.75 |
| 10-24 15:17 | +5 | NEAR | DOWN | 0.51 | 0.62 | 0.75 |
| 10-24 15:16 | +10 stop | SOL | DOWN | 0.70 | open |  |
| 10-24 15:16 | +20 | SOL | DOWN | 0.71 | open |  |
| 10-24 15:16 | +15 | SOL | DOWN | 0.71 | open |  |
| 10-24 15:16 | +10 | SOL | DOWN | 0.71 | open |  |
| 10-24 15:16 | +5 | SOL | DOWN | 0.69 | 0.77 | 0.52 |
| 10-24 15:15 | +10 stop | BNB | DOWN | 0.69 | 0.83 | 1.15 |
| 10-24 15:15 | +20 | BNB | DOWN | 0.69 | 0.91 | 1.95 |
| 10-24 15:15 | +15 | BNB | DOWN | 0.69 | 0.84 | 1.25 |
| 10-24 15:15 | +10 | BNB | DOWN | 0.69 | 0.83 | 1.15 |
| 10-24 15:15 | +5 | BNB | DOWN | 0.69 | 0.83 | 1.15 |
| 10-24 15:12 | +10 stop | ZEC | DOWN | 0.61 | 0.76 | 1.24 |
| 10-24 15:10 | +10 stop | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 10-24 15:07 | +10 stop | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 10-24 15:06 | +10 stop | NEAR | DOWN | 0.49 | 0.67 | 1.46 |
| 10-24 15:05 | +10 stop | ZEC | UP | 0.49 | 0.63 | 1.05 |
| 10-24 15:03 | +10 stop | ZEC | DOWN | 0.61 | 0.40 | -2.44 |
| 10-24 15:02 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-24 15:02 | +10 | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-24 15:02 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 10-24 15:02 | +10 stop | ZEC | DOWN | 0.51 | 0.61 | 0.65 |
| 10-24 15:02 | +10 stop | XRP | DOWN | 0.64 | 0.78 | 1.10 |
| 10-24 15:02 | +10 stop | NEAR | DOWN | 0.50 | 0.64 | 1.05 |
| 10-24 15:02 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
