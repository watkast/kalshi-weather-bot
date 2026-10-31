# Range-Scalp Bot

*Updated Sat Oct 31 10:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42101 | 36728 | 5373 (55) | 2 | $-11846.88 | -4.5% |
| **+10¢** | 31385 | 25166 | 6219 (79) | 3 | $-10600.42 | -5.4% |
| **+15¢** | 26239 | 19533 | 6706 (107) | 5 | $-9709.84 | -5.9% |
| **+20¢** | 23304 | 16281 | 7023 (138) | 5 | $-8551.46 | -5.8% |
| **+10¢ (15¢ stop)** | 51337 | 51262 | 75 (41) | 2 | $-19385.70 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 10:03 | +10 stop | BNB | DOWN | 0.71 | open |  |
| 10-31 10:02 | +10 stop | SOL | DOWN | 0.65 | open |  |
| 10-31 10:02 | +10 stop | ZEC | DOWN | 0.58 | 0.69 | 0.77 |
| 10-31 10:02 | +10 stop | BNB | DOWN | 0.55 | 0.66 | 0.76 |
| 10-31 10:02 | +5 | ZEC | DOWN | 0.60 | 0.66 | 0.27 |
| 10-31 10:02 | +10 stop | XRP | DOWN | 0.62 | 0.73 | 0.82 |
| 10-31 10:02 | +20 | XRP | DOWN | 0.61 | open |  |
| 10-31 10:02 | +15 | XRP | DOWN | 0.61 | open |  |
| 10-31 10:02 | +10 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-31 10:02 | +5 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-31 10:02 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-31 10:02 | +20 | HYPE | DOWN | 0.64 | 0.85 | 1.81 |
| 10-31 10:02 | +15 | HYPE | DOWN | 0.64 | 0.85 | 1.80 |
| 10-31 10:02 | +10 | HYPE | DOWN | 0.64 | 0.77 | 0.96 |
| 10-31 10:02 | +5 | HYPE | DOWN | 0.64 | 0.77 | 0.96 |
| 10-31 10:02 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-31 10:02 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-31 10:02 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-31 10:02 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-31 10:02 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 10-31 10:01 | +10 stop | ZEC | UP | 0.62 | 0.40 | -2.53 |
| 10-31 10:01 | +20 | ZEC | UP | 0.62 | open |  |
| 10-31 10:01 | +15 | ZEC | UP | 0.61 | open |  |
| 10-31 10:01 | +10 | ZEC | UP | 0.64 | open |  |
| 10-31 10:01 | +5 | ZEC | UP | 0.64 | 0.70 | 0.28 |
| 10-31 10:01 | +10 stop | BNB | UP | 0.58 | 0.42 | -1.96 |
| 10-31 10:01 | +20 | BNB | UP | 0.58 | open |  |
| 10-31 10:01 | +15 | BNB | UP | 0.58 | open |  |
| 10-31 10:01 | +10 | BNB | UP | 0.58 | open |  |
| 10-31 10:01 | +5 | BNB | UP | 0.58 | open |  |
| 10-31 10:01 | +10 stop | SOL | UP | 0.68 | 0.47 | -2.44 |
| 10-31 10:01 | +20 | SOL | UP | 0.68 | open |  |
| 10-31 10:01 | +15 | SOL | UP | 0.69 | open |  |
| 10-31 10:01 | +10 | SOL | UP | 0.69 | open |  |
| 10-31 10:01 | +5 | SOL | UP | 0.69 | open |  |
| 10-31 10:01 | +10 stop | BTC | DOWN | 0.58 | 0.71 | 0.97 |
| 10-31 10:01 | +20 | BTC | DOWN | 0.58 | 0.79 | 1.80 |
| 10-31 10:01 | +15 | BTC | DOWN | 0.58 | 0.77 | 1.59 |
| 10-31 10:01 | +10 | BTC | DOWN | 0.58 | 0.71 | 0.97 |
| 10-31 10:01 | +5 | BTC | DOWN | 0.58 | 0.71 | 0.97 |
