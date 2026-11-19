# Range-Scalp Bot

*Updated Thu Nov 19 23:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65450 | 57137 | 8313 (124) | 1 | $-17494.01 | -4.2% |
| **+10¢** | 48872 | 39150 | 9722 (165) | 3 | $-16278.10 | -5.3% |
| **+15¢** | 40984 | 30496 | 10488 (211) | 3 | $-14649.35 | -5.7% |
| **+20¢** | 36490 | 25470 | 11020 (266) | 3 | $-12982.23 | -5.7% |
| **+10¢ (15¢ stop)** | 79679 | 79515 | 164 (98) | 3 | $-29320.99 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 23:01 | +10 stop | ZEC | UP | 0.48 | open |  |
| 11-19 23:01 | +20 | ZEC | UP | 0.48 | open |  |
| 11-19 23:01 | +15 | ZEC | UP | 0.50 | open |  |
| 11-19 23:01 | +10 | ZEC | UP | 0.50 | open |  |
| 11-19 23:01 | +5 | ZEC | UP | 0.50 | open |  |
| 11-19 23:01 | +10 stop | SOL | UP | 0.59 | open |  |
| 11-19 23:01 | +20 | SOL | UP | 0.59 | open |  |
| 11-19 23:01 | +15 | SOL | UP | 0.59 | open |  |
| 11-19 23:01 | +10 | SOL | UP | 0.59 | open |  |
| 11-19 23:01 | +5 | SOL | UP | 0.59 | 0.64 | 0.16 |
| 11-19 23:01 | +10 stop | NEAR | UP | 0.69 | open |  |
| 11-19 23:01 | +20 | NEAR | UP | 0.69 | open |  |
| 11-19 23:01 | +15 | NEAR | UP | 0.69 | open |  |
| 11-19 23:01 | +10 | NEAR | UP | 0.69 | open |  |
| 11-19 23:01 | +5 | NEAR | UP | 0.69 | 0.77 | 0.52 |
| 11-19 22:58 | +10 stop | NEAR | UP | 0.68 | 0.83 | 1.24 |
| 11-19 22:58 | +20 | NEAR | UP | 0.69 | 0.97 | 2.63 |
| 11-19 22:58 | +15 | NEAR | UP | 0.70 | 0.97 | 2.55 |
| 11-19 22:58 | +10 | NEAR | UP | 0.67 | 0.83 | 1.34 |
| 11-19 22:58 | +5 | NEAR | UP | 0.66 | 0.83 | 1.45 |
| 11-19 22:58 | +10 stop | BNB | DOWN | 0.56 | 0.99 | 4.05 |
| 11-19 22:58 | +10 stop | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-19 22:56 | +10 stop | SOL | DOWN | 0.63 | 0.47 | -1.95 |
| 11-19 22:56 | +20 | SOL | DOWN | 0.63 | yes | -6.47 |
| 11-19 22:56 | +15 | SOL | DOWN | 0.63 | yes | -6.47 |
| 11-19 22:56 | +10 | SOL | DOWN | 0.63 | yes | -6.47 |
| 11-19 22:56 | +5 | SOL | DOWN | 0.63 | yes | -6.47 |
| 11-19 22:56 | +10 stop | HYPE | DOWN | 0.58 | 0.39 | -2.25 |
| 11-19 22:54 | +10 stop | HYPE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-19 22:53 | +10 stop | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-19 22:52 | +5 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 11-19 22:52 | +10 stop | HYPE | UP | 0.54 | 0.33 | -2.45 |
| 11-19 22:52 | +15 | HYPE | UP | 0.54 | 0.80 | 2.29 |
| 11-19 22:52 | +10 | HYPE | UP | 0.55 | 0.67 | 0.85 |
| 11-19 22:52 | +5 | HYPE | UP | 0.56 | 0.65 | 0.57 |
| 11-19 22:51 | +10 stop | SOL | DOWN | 0.60 | 0.72 | 0.88 |
| 11-19 22:51 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-19 22:50 | +10 stop | ETH | DOWN | 0.56 | 0.71 | 1.17 |
| 11-19 22:50 | +10 stop | XRP | DOWN | 0.63 | 0.81 | 1.50 |
| 11-19 22:50 | +10 stop | DOGE | DOWN | 0.61 | 0.75 | 1.09 |
