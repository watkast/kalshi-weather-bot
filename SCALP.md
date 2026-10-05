# Range-Scalp Bot

*Updated Mon Oct 05 11:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3720 | 3200 | 520 (3) | 1 | $-1305.39 | -5.6% |
| **+10¢** | 2879 | 2281 | 598 (4) | 0 | $-1182.69 | -6.5% |
| **+15¢** | 2417 | 1788 | 629 (7) | 1 | $-1018.46 | -6.7% |
| **+20¢** | 2159 | 1504 | 655 (12) | 1 | $-850.40 | -6.3% |
| **+10¢ (15¢ stop)** | 4606 | 4605 | 1 (1) | 0 | $-1740.02 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 11:02 | +10 stop | BNB | UP | 0.49 | 0.32 | -2.04 |
| 10-05 11:02 | +5 | NEAR | DOWN | 0.63 | 0.69 | 0.28 |
| 10-05 11:01 | +10 stop | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 10-05 11:01 | +20 | NEAR | DOWN | 0.55 | 0.78 | 1.99 |
| 10-05 11:01 | +15 | NEAR | DOWN | 0.55 | 0.71 | 1.27 |
| 10-05 11:01 | +10 | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 10-05 11:01 | +5 | NEAR | DOWN | 0.53 | 0.61 | 0.45 |
| 10-05 11:01 | +10 stop | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 11:01 | +20 | XRP | DOWN | 0.62 | 0.82 | 1.72 |
| 10-05 11:01 | +15 | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 11:01 | +10 | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 11:01 | +5 | XRP | DOWN | 0.62 | 0.71 | 0.58 |
| 10-05 11:01 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-05 11:01 | +20 | BTC | DOWN | 0.67 | 0.87 | 1.76 |
| 10-05 11:01 | +15 | BTC | DOWN | 0.67 | 0.85 | 1.55 |
| 10-05 11:01 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-05 11:01 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-05 11:01 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-05 11:01 | +20 | ZEC | DOWN | 0.58 | 0.80 | 1.90 |
| 10-05 11:01 | +15 | ZEC | DOWN | 0.58 | 0.75 | 1.38 |
| 10-05 11:01 | +10 | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-05 11:01 | +5 | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-05 11:01 | +10 stop | DOGE | DOWN | 0.57 | 0.71 | 1.11 |
| 10-05 11:01 | +20 | DOGE | DOWN | 0.57 | 0.81 | 2.16 |
| 10-05 11:01 | +15 | DOGE | DOWN | 0.57 | 0.75 | 1.52 |
| 10-05 11:01 | +10 | DOGE | DOWN | 0.57 | 0.71 | 1.11 |
| 10-05 11:01 | +5 | DOGE | DOWN | 0.57 | 0.71 | 1.11 |
| 10-05 11:01 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-05 11:01 | +20 | SOL | DOWN | 0.70 | 0.90 | 1.78 |
| 10-05 11:01 | +15 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 10-05 11:01 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-05 11:01 | +5 | SOL | DOWN | 0.70 | 0.75 | 0.21 |
| 10-05 11:01 | +5 | BNB | UP | 0.61 | open |  |
| 10-05 11:00 | +10 stop | BNB | DOWN | 0.55 | 0.39 | -1.95 |
| 10-05 11:00 | +20 | BNB | DOWN | 0.55 | open |  |
| 10-05 11:00 | +15 | BNB | DOWN | 0.56 | open |  |
| 10-05 11:00 | +10 | BNB | DOWN | 0.57 | 0.67 | 0.67 |
| 10-05 11:00 | +5 | BNB | DOWN | 0.57 | 0.64 | 0.36 |
| 10-05 10:46 | +10 stop | BNB | UP | 0.57 | 0.70 | 0.97 |
| 10-05 10:46 | +20 | BNB | UP | 0.57 | 0.83 | 2.32 |
