# Range-Scalp Bot

*Updated Thu Oct 15 19:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18027 | 15648 | 2379 (28) | 0 | $-5536.03 | -4.9% |
| **+10¢** | 13618 | 10863 | 2755 (40) | 0 | $-5024.14 | -5.9% |
| **+15¢** | 11420 | 8457 | 2963 (59) | 1 | $-4532.99 | -6.3% |
| **+20¢** | 10150 | 7051 | 3099 (77) | 3 | $-3941.52 | -6.2% |
| **+10¢ (15¢ stop)** | 22185 | 22135 | 50 (29) | 1 | $-8586.30 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 19:33 | +10 stop | ZEC | DOWN | 0.66 | open |  |
| 10-15 19:33 | +10 | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-15 19:33 | +5 | ZEC | DOWN | 0.66 | 0.75 | 0.60 |
| 10-15 19:32 | +10 | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 10-15 19:32 | +5 | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 10-15 19:32 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-15 19:31 | +10 stop | NEAR | DOWN | 0.71 | 0.85 | 1.16 |
| 10-15 19:31 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-15 19:31 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-15 19:31 | +10 | NEAR | DOWN | 0.71 | 0.85 | 1.16 |
| 10-15 19:31 | +5 | NEAR | DOWN | 0.69 | 0.80 | 0.83 |
| 10-15 19:31 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.28 |
| 10-15 19:31 | +10 stop | BNB | DOWN | 0.60 | 0.70 | 0.69 |
| 10-15 19:31 | +20 | BNB | DOWN | 0.60 | open |  |
| 10-15 19:31 | +15 | BNB | DOWN | 0.60 | 0.78 | 1.53 |
| 10-15 19:31 | +10 | BNB | DOWN | 0.58 | 0.69 | 0.77 |
| 10-15 19:31 | +5 | BNB | DOWN | 0.58 | 0.64 | 0.25 |
| 10-15 19:31 | +10 stop | ZEC | DOWN | 0.59 | 0.73 | 1.09 |
| 10-15 19:31 | +20 | ZEC | DOWN | 0.59 | open |  |
| 10-15 19:31 | +15 | ZEC | DOWN | 0.59 | 0.75 | 1.29 |
| 10-15 19:31 | +10 | ZEC | DOWN | 0.59 | 0.73 | 1.09 |
| 10-15 19:31 | +5 | ZEC | DOWN | 0.59 | 0.65 | 0.27 |
| 10-15 19:26 | +10 stop | HYPE | UP | 0.71 | 0.88 | 1.47 |
| 10-15 19:26 | +5 | HYPE | UP | 0.71 | 0.79 | 0.53 |
| 10-15 19:25 | +10 stop | SOL | UP | 0.58 | 0.79 | 1.80 |
| 10-15 19:25 | +20 | SOL | UP | 0.58 | 0.79 | 1.80 |
| 10-15 19:25 | +15 | SOL | UP | 0.58 | 0.79 | 1.80 |
| 10-15 19:25 | +10 | SOL | UP | 0.58 | 0.79 | 1.80 |
| 10-15 19:25 | +5 | SOL | UP | 0.57 | 0.79 | 1.90 |
| 10-15 19:24 | +10 stop | BNB | DOWN | 0.66 | 0.48 | -2.14 |
| 10-15 19:23 | +10 stop | HYPE | UP | 0.64 | 0.75 | 0.79 |
| 10-15 19:22 | +15 | HYPE | UP | 0.66 | 0.88 | 1.96 |
| 10-15 19:22 | +10 | HYPE | UP | 0.66 | 0.79 | 1.02 |
| 10-15 19:22 | +5 | HYPE | UP | 0.66 | 0.75 | 0.60 |
| 10-15 19:22 | +10 stop | BNB | UP | 0.52 | 0.30 | -2.53 |
| 10-15 19:22 | +10 | BNB | UP | 0.52 | no | -5.38 |
| 10-15 19:22 | +5 | BNB | UP | 0.52 | no | -5.38 |
| 10-15 19:20 | +10 | HYPE | UP | 0.63 | 0.76 | 1.00 |
| 10-15 19:19 | +5 | HYPE | UP | 0.71 | 0.76 | 0.22 |
| 10-15 19:19 | +10 stop | HYPE | UP | 0.71 | 0.52 | -2.23 |
