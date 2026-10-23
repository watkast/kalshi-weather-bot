# Range-Scalp Bot

*Updated Fri Oct 23 01:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29589 | 25751 | 3838 (39) | 3 | $-8760.42 | -4.7% |
| **+10¢** | 22191 | 17749 | 4442 (55) | 3 | $-7884.36 | -5.6% |
| **+15¢** | 18576 | 13807 | 4769 (78) | 6 | $-7072.79 | -6.1% |
| **+20¢** | 16437 | 11439 | 4998 (100) | 9 | $-6412.96 | -6.2% |
| **+10¢ (15¢ stop)** | 36340 | 36281 | 59 (32) | 3 | $-13727.16 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 01:33 | +10 stop | NEAR | DOWN | 0.65 | open |  |
| 10-23 01:33 | +20 | NEAR | DOWN | 0.65 | open |  |
| 10-23 01:33 | +15 | NEAR | DOWN | 0.65 | open |  |
| 10-23 01:33 | +10 | NEAR | DOWN | 0.65 | open |  |
| 10-23 01:33 | +5 | NEAR | DOWN | 0.65 | open |  |
| 10-23 01:33 | +10 stop | ZEC | DOWN | 0.69 | open |  |
| 10-23 01:32 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 10-23 01:32 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-23 01:32 | +5 | BNB | DOWN | 0.70 | open |  |
| 10-23 01:31 | +10 stop | ZEC | UP | 0.61 | 0.44 | -2.05 |
| 10-23 01:31 | +20 | ZEC | UP | 0.61 | open |  |
| 10-23 01:31 | +15 | ZEC | UP | 0.61 | open |  |
| 10-23 01:31 | +10 | ZEC | UP | 0.61 | open |  |
| 10-23 01:31 | +5 | ZEC | UP | 0.61 | open |  |
| 10-23 01:31 | +10 stop | BNB | DOWN | 0.57 | 0.69 | 0.84 |
| 10-23 01:31 | +20 | BNB | DOWN | 0.57 | open |  |
| 10-23 01:31 | +15 | BNB | DOWN | 0.57 | open |  |
| 10-23 01:31 | +10 | BNB | DOWN | 0.57 | 0.69 | 0.84 |
| 10-23 01:31 | +5 | BNB | DOWN | 0.57 | 0.69 | 0.84 |
| 10-23 01:31 | +10 stop | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 10-23 01:31 | +20 | BTC | DOWN | 0.65 | open |  |
| 10-23 01:31 | +15 | BTC | DOWN | 0.65 | open |  |
| 10-23 01:31 | +10 | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 10-23 01:31 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-23 01:31 | +10 stop | DOGE | DOWN | 0.68 | 0.80 | 0.92 |
| 10-23 01:31 | +20 | DOGE | DOWN | 0.68 | open |  |
| 10-23 01:31 | +15 | DOGE | DOWN | 0.68 | open |  |
| 10-23 01:31 | +10 | DOGE | DOWN | 0.68 | 0.80 | 0.92 |
| 10-23 01:31 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-23 01:31 | +10 stop | SOL | DOWN | 0.61 | 0.76 | 1.20 |
| 10-23 01:31 | +20 | SOL | DOWN | 0.61 | open |  |
| 10-23 01:31 | +15 | SOL | DOWN | 0.61 | 0.76 | 1.20 |
| 10-23 01:31 | +10 | SOL | DOWN | 0.61 | 0.76 | 1.20 |
| 10-23 01:31 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 10-23 01:31 | +10 stop | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 10-23 01:31 | +20 | ETH | DOWN | 0.62 | open |  |
| 10-23 01:31 | +15 | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 10-23 01:31 | +10 | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 10-23 01:31 | +5 | ETH | DOWN | 0.62 | 0.68 | 0.27 |
| 10-23 01:31 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
