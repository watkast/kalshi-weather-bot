# Range-Scalp Bot

*Updated Sun Nov 15 13:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60836 | 53077 | 7759 (112) | 5 | $-16453.18 | -4.3% |
| **+10¢** | 45451 | 36353 | 9098 (150) | 6 | $-15521.37 | -5.4% |
| **+15¢** | 38068 | 28256 | 9812 (188) | 6 | $-14186.68 | -5.9% |
| **+20¢** | 33926 | 23634 | 10292 (240) | 6 | $-12473.47 | -5.9% |
| **+10¢ (15¢ stop)** | 74035 | 73884 | 151 (89) | 4 | $-27211.30 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 13:31 | +5 | ETH | DOWN | 0.66 | 0.73 | 0.40 |
| 11-15 13:31 | +10 stop | XRP | DOWN | 0.67 | open |  |
| 11-15 13:31 | +10 stop | BNB | DOWN | 0.71 | 0.53 | -2.13 |
| 11-15 13:31 | +20 | BNB | DOWN | 0.71 | open |  |
| 11-15 13:31 | +15 | BNB | DOWN | 0.71 | open |  |
| 11-15 13:31 | +10 | BNB | DOWN | 0.71 | open |  |
| 11-15 13:31 | +5 | BNB | DOWN | 0.71 | open |  |
| 11-15 13:31 | +10 stop | NEAR | UP | 0.51 | open |  |
| 11-15 13:31 | +20 | NEAR | UP | 0.51 | open |  |
| 11-15 13:31 | +15 | NEAR | UP | 0.51 | open |  |
| 11-15 13:31 | +10 | NEAR | UP | 0.51 | open |  |
| 11-15 13:31 | +5 | NEAR | UP | 0.51 | open |  |
| 11-15 13:31 | +5 | DOGE | DOWN | 0.63 | open |  |
| 11-15 13:31 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 11-15 13:31 | +20 | ETH | DOWN | 0.68 | open |  |
| 11-15 13:31 | +15 | ETH | DOWN | 0.68 | open |  |
| 11-15 13:31 | +10 | ETH | DOWN | 0.68 | open |  |
| 11-15 13:31 | +5 | ETH | DOWN | 0.68 | 0.74 | 0.30 |
| 11-15 13:31 | +10 stop | XRP | DOWN | 0.69 | 0.54 | -1.83 |
| 11-15 13:31 | +20 | XRP | DOWN | 0.69 | open |  |
| 11-15 13:31 | +15 | XRP | DOWN | 0.68 | open |  |
| 11-15 13:31 | +10 | XRP | DOWN | 0.66 | open |  |
| 11-15 13:31 | +5 | XRP | DOWN | 0.66 | open |  |
| 11-15 13:31 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 11-15 13:31 | +20 | BTC | DOWN | 0.70 | open |  |
| 11-15 13:31 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-15 13:31 | +10 | BTC | DOWN | 0.71 | open |  |
| 11-15 13:31 | +5 | BTC | DOWN | 0.71 | open |  |
| 11-15 13:30 | +10 stop | DOGE | DOWN | 0.69 | 0.45 | -2.73 |
| 11-15 13:30 | +20 | DOGE | DOWN | 0.69 | open |  |
| 11-15 13:30 | +15 | DOGE | DOWN | 0.70 | open |  |
| 11-15 13:30 | +10 | DOGE | DOWN | 0.71 | open |  |
| 11-15 13:27 | +10 stop | SOL | UP | 0.70 | 0.55 | -1.83 |
| 11-15 13:27 | +5 | SOL | UP | 0.70 | 0.77 | 0.42 |
| 11-15 13:26 | +10 stop | BNB | DOWN | 0.68 | 0.82 | 1.12 |
| 11-15 13:26 | +20 | BNB | DOWN | 0.68 | 0.97 | 2.71 |
| 11-15 13:26 | +15 | BNB | DOWN | 0.70 | 0.87 | 1.47 |
| 11-15 13:25 | +10 stop | ETH | UP | 0.65 | 0.81 | 1.33 |
| 11-15 13:24 | +5 | BNB | DOWN | 0.65 | 0.80 | 1.22 |
| 11-15 13:23 | +10 stop | BNB | DOWN | 0.56 | 0.80 | 2.10 |
